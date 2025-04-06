"""
Simplified robustness testing suite for machine learning models.

This module provides a streamlined interface for testing model robustness
against feature perturbations using DBDataset objects.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Union, Any, Tuple
import time
import datetime
import os

from deepbridge.validation.wrappers.robustness import (
    DataPerturber, 
    RobustnessEvaluator, 
    RobustnessVisualizer, 
    RobustnessReporter
)

class RobustnessSuite:
    """
    Focused suite for model robustness testing with Gaussian noise and Quantile perturbation.
    This class has been refactored to use specialized components for data perturbation,
    robustness evaluation, visualization, and reporting.
    """
    
    # Predefined configurations with varying perturbation levels
    _CONFIG_TEMPLATES = {
        'quick': [
            {'type': 'raw', 'params': {'level': 0.1}},
            {'type': 'raw', 'params': {'level': 0.2}},
            {'type': 'quantile', 'params': {'level': 0.1}},
            {'type': 'quantile', 'params': {'level': 0.2}}
        ],
        
        'medium': [
            {'type': 'raw', 'params': {'level': 0.1}},
            {'type': 'raw', 'params': {'level': 0.2}},
            {'type': 'raw', 'params': {'level': 0.4}},
            {'type': 'quantile', 'params': {'level': 0.1}},
            {'type': 'quantile', 'params': {'level': 0.2}},
            {'type': 'quantile', 'params': {'level': 0.4}}
        ],
        
        'full': [
            {'type': 'raw', 'params': {'level': 0.1}},
            {'type': 'raw', 'params': {'level': 0.2}},
            {'type': 'raw', 'params': {'level': 0.4}},
            {'type': 'raw', 'params': {'level': 0.6}},
            {'type': 'raw', 'params': {'level': 0.8}},
            {'type': 'raw', 'params': {'level': 1.0}},
            {'type': 'quantile', 'params': {'level': 0.1}},
            {'type': 'quantile', 'params': {'level': 0.2}},
            {'type': 'quantile', 'params': {'level': 0.4}},
            {'type': 'quantile', 'params': {'level': 0.6}},
            {'type': 'quantile', 'params': {'level': 0.8}},
            {'type': 'quantile', 'params': {'level': 1.0}}
        ]
    }
    
    def __init__(self, dataset, verbose: bool = False, metric: str = 'AUC', feature_subset: Optional[List[str]] = None, random_state: Optional[int] = None):
        """
        Initialize the robustness testing suite.
        
        Parameters:
        -----------
        dataset : DBDataset
            Dataset object containing training/test data and model
        verbose : bool
            Whether to print progress information
        metric : str
            Performance metric to use for evaluation ('AUC', 'accuracy', 'mse', etc.)
        feature_subset : List[str] or None
            Subset of features to test (None for all features)
        random_state : int or None
            Random seed for reproducibility
        """
        self.dataset = dataset
        self.verbose = verbose
        self.feature_subset = feature_subset
        self.metric = metric
        
        # Initialize components
        self.data_perturber = DataPerturber()
        if random_state is not None:
            self.data_perturber.set_random_state(random_state)
            
        self.evaluator = RobustnessEvaluator(dataset, metric, verbose, random_state)
        self.visualizer = RobustnessVisualizer()
        self.reporter = RobustnessReporter(verbose)
        
        # Store current configuration
        self.current_config = None
        
        # Store results
        self.results = {}
        
        if self.verbose:
            print(f"Robustness Suite initialized with metric: {self.metric}")
    
    def config(self, config_name: str = 'quick', feature_subset: Optional[List[str]] = None) -> 'RobustnessSuite':
        """
        Set a predefined configuration for robustness tests.
        
        Parameters:
        -----------
        config_name : str
            Name of the configuration to use: 'quick', 'medium', or 'full'
        feature_subset : List[str] or None
            Subset of features to test (overrides the one set in constructor)
                
        Returns:
        --------
        self : Returns self to allow method chaining
        """
        self.feature_subset = feature_subset if feature_subset is not None else self.feature_subset

        if config_name not in self._CONFIG_TEMPLATES:
            raise ValueError(f"Unknown configuration: {config_name}. Available options: {list(self._CONFIG_TEMPLATES.keys())}")
        
        # Clone the configuration template
        self.current_config = self._clone_config(self._CONFIG_TEMPLATES[config_name])
        
        # Update feature_subset in tests if specified
        if self.feature_subset:
            for test in self.current_config:
                if 'params' in test:
                    test['params']['feature_subset'] = self.feature_subset
        
        if self.verbose:
            print(f"\nConfigured for {config_name} robustness test suite")
            if self.feature_subset:
                print(f"Feature subset: {self.feature_subset}")
            print(f"\nTests that will be executed:")
            
            # Print all configured tests
            for i, test in enumerate(self.current_config, 1):
                test_type = test['type']
                params = test.get('params', {})
                param_str = ', '.join(f"{k}={v}" for k, v in params.items() if k != 'feature_subset')
                print(f"  {i}. {test_type} ({param_str})")
        
        return self
    
    def _clone_config(self, config):
        """Clone configuration to avoid modifying original templates."""
        import copy
        return copy.deepcopy(config)
    
    def run(self, X: Optional[pd.DataFrame] = None, y: Optional[pd.Series] = None) -> Dict[str, Any]:
        """
        Run the configured robustness tests.
        
        Parameters:
        -----------
        X : DataFrame, optional
            Feature data to use (if None, will use test data from dataset)
        y : Series, optional
            Target variable (if None, will use test target from dataset)
            
        Returns:
        --------
        Dict[str, Any] : Dictionary with test results
        """
        if self.current_config is None:
            # Use default configuration if none specified
            self.config('quick')
            
        if X is None or y is None:
            # Use test data from dataset if not provided
            if hasattr(self.dataset, 'test_data') and self.dataset.test_data is not None:
                X = self.dataset.get_feature_data('test')
                y = self.dataset.get_target_data('test')
            else:
                raise ValueError("No test data available in dataset. Please provide X and y.")
        
        # Track execution time
        start_time = time.time()
        
        if self.verbose:
            print(f"\nRunning robustness tests on dataset with {X.shape[0]} rows and {X.shape[1]} columns")
            
        # Initialize results structure
        results = {
            'base_score': 0,
            'raw': {'by_level': {}, 'overall': {}},
            'quantile': {'by_level': {}, 'overall': {}},
            'feature_importance': {},
            'visualizations': {}
        }
        
        # Calculate baseline score
        base_score = self.evaluator.calculate_base_score(X, y)
        results['base_score'] = base_score
        
        if self.verbose:
            print(f"Baseline score: {base_score:.3f}")
            
        # Process each test configuration
        all_raw_impacts = []
        all_quantile_impacts = []
        all_impacts = []
        
        for test_idx, test_config in enumerate(self.current_config, 1):
            test_type = test_config['type']
            params = test_config.get('params', {})
            
            # Extract parameters with defaults
            level = params.get('level', 0.1)
            test_feature_subset = params.get('feature_subset', self.feature_subset)
            
            if self.verbose:
                print(f"\nRunning test {test_idx}/{len(self.current_config)}: {test_type}, level={level}")
                
            # Evaluate perturbation
            eval_result = self.evaluator.evaluate_perturbation(
                X, y, test_type, level, test_feature_subset
            )
            
            # Store result by level
            level_key = str(level)
            if test_type == 'raw':
                if level_key not in results['raw']['by_level']:
                    results['raw']['by_level'][level_key] = {'runs': [], 'overall_result': {}}
                
                results['raw']['by_level'][level_key]['runs'].append(eval_result)
                all_raw_impacts.append(eval_result['impact'])
                all_impacts.append(eval_result['impact'])
                
                # Calculate overall result for this level
                runs = results['raw']['by_level'][level_key]['runs']
                mean_score = np.mean([run['perturbed_score'] for run in runs])
                std_score = np.std([run['perturbed_score'] for run in runs])
                
                results['raw']['by_level'][level_key]['overall_result'] = {
                    'mean_score': mean_score,
                    'std_score': std_score,
                    'impact': np.mean([run['impact'] for run in runs])
                }
                
            elif test_type == 'quantile':
                if level_key not in results['quantile']['by_level']:
                    results['quantile']['by_level'][level_key] = {'runs': [], 'overall_result': {}}
                
                results['quantile']['by_level'][level_key]['runs'].append(eval_result)
                all_quantile_impacts.append(eval_result['impact'])
                all_impacts.append(eval_result['impact'])
                
                # Calculate overall result for this level
                runs = results['quantile']['by_level'][level_key]['runs']
                mean_score = np.mean([run['perturbed_score'] for run in runs])
                std_score = np.std([run['perturbed_score'] for run in runs])
                
                results['quantile']['by_level'][level_key]['overall_result'] = {
                    'mean_score': mean_score,
                    'std_score': std_score,
                    'impact': np.mean([run['impact'] for run in runs])
                }
        
        # Evaluate feature importance using the median level from configurations
        if self.verbose:
            print("\nEvaluating feature importance...")
            
        # Find the median level for raw perturbation
        raw_levels = [test['params'].get('level', 0.1) for test in self.current_config if test['type'] == 'raw']
        if raw_levels:
            median_level = np.median(raw_levels)
            
            # Evaluate feature importance
            feature_importance = self.evaluator.evaluate_feature_importance(
                X, y, 'raw', median_level, self.feature_subset
            )
            
            results['feature_importance'] = feature_importance
        
        # Calculate average impacts
        results['avg_raw_impact'] = np.mean(all_raw_impacts) if all_raw_impacts else 0
        results['avg_quantile_impact'] = np.mean(all_quantile_impacts) if all_quantile_impacts else 0
        results['avg_overall_impact'] = np.mean(all_impacts) if all_impacts else 0
        
        # Create visualizations
        if self.verbose:
            print("\nGenerating visualizations...")
            
        # Generate score distribution plot
        results['visualizations']['score_distribution'] = self.visualizer.create_score_distribution_plot(results)
        
        # Generate feature importance plot if available
        if results['feature_importance']:
            results['visualizations']['feature_importance'] = self.visualizer.create_feature_importance_plot(
                results['feature_importance']
            )
        
        # Generate methods comparison plot
        results['visualizations']['perturbation_methods'] = self.visualizer.create_methods_comparison_plot(results)
        
        # Record execution time
        execution_time = time.time() - start_time
        results['execution_time'] = execution_time
        
        if self.verbose:
            print(f"\nTests completed in {execution_time:.2f} seconds")
            print(f"Average raw impact: {results['avg_raw_impact']:.3f}")
            print(f"Average quantile impact: {results['avg_quantile_impact']:.3f}")
            print(f"Overall average impact: {results['avg_overall_impact']:.3f}")
        
        # Store results
        self.results = results
        
        return results
    
    def compare(self, alternative_models: Dict[str, Any], X: Optional[pd.DataFrame] = None, y: Optional[pd.Series] = None) -> Dict[str, Dict[str, Any]]:
        """
        Compare robustness of multiple models using the same configuration.
        
        Parameters:
        -----------
        alternative_models : Dict
            Dictionary mapping model names to model objects
        X : DataFrame, optional
            Feature data to use (if None, will use test data from dataset)
        y : Series, optional
            Target variable (if None, will use test target from dataset)
            
        Returns:
        --------
        Dict[str, Dict[str, Any]] : Dictionary mapping model names to test results
        """
        if not alternative_models:
            raise ValueError("No alternative models provided")
        
        if self.current_config is None:
            # Use default configuration if none specified
            self.config('quick')
            
        if X is None or y is None:
            # Use test data from dataset if not provided
            if hasattr(self.dataset, 'test_data') and self.dataset.test_data is not None:
                X = self.dataset.get_feature_data('test')
                y = self.dataset.get_target_data('test')
            else:
                raise ValueError("No test data available in dataset. Please provide X and y.")
        
        # Run tests for primary model first
        primary_results = self.run(X, y)
        
        # Store results
        all_results = {
            'primary_model': primary_results
        }
        
        # Test alternative models
        for model_name, model in alternative_models.items():
            if self.verbose:
                print(f"\nTesting robustness of alternative model: {model_name}")
            
            # Create a temporary dataset with the alternative model
            original_model = self.dataset.model
            self.dataset.model = model
            
            # Run the same tests on this model
            model_results = self.run(X, y)
            
            # Restore original model
            self.dataset.model = original_model
            
            # Store results
            all_results[model_name] = model_results
        
        # Create model comparison visualization
        if self.verbose:
            print("\nGenerating model comparison visualization...")
            
        # Generate model comparison plot
        model_comparison = self.visualizer.create_model_comparison_plot(
            primary_results,
            {name: results for name, results in all_results.items() if name != 'primary_model'}
        )
        
        # Add to primary model results
        all_results['primary_model']['visualizations']['models_comparison'] = model_comparison
        
        # Update stored results
        self.results = all_results['primary_model']
        
        return all_results
    
    def save_report(self, output_path: str = None, model_name: str = "Main Model", format: str = "html") -> str:
        """
        Generate and save a report with the test results.
        
        Parameters:
        -----------
        output_path : str, optional
            Path to save the report (if None, will use default path)
        model_name : str
            Name of the model for the report
        format : str
            Report format ('text' or 'html')
            
        Returns:
        --------
        str : Path to the saved report
        """
        if not self.results:
            raise ValueError("No results available. Run tests first.")
        
        # Use default path if none provided
        if output_path is None:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            model_name_clean = model_name.replace(' ', '_').lower()
            output_path = f"robustness_report_{model_name_clean}_{timestamp}.{'html' if format == 'html' else 'txt'}"
            
        # Ensure directory exists
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        
        if format.lower() == 'html':
            # Generate HTML report
            return self.reporter.save_html_report(
                output_path,
                self.results,
                self.results.get('visualizations', {}),
                model_name
            )
        else:
            # Generate text report
            return self.reporter.save_text_report(
                output_path,
                self.results,
                model_name
            )
    
    def get_results(self) -> Dict[str, Any]:
        """Get the test results."""
        return self.results
    
    def get_visualizations(self) -> Dict[str, Any]:
        """Get the visualizations generated during testing."""
        return self.results.get('visualizations', {})