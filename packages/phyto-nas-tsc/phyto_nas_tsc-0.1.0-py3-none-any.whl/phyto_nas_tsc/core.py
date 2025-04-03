from ._optimizer import NASOptimizer
from ._data_handler import validate_inputs

def fit(X=None, y=None, scoring='accuracy', data_dir=None, population_size=15, generations=5, **kwargs):
    """
    Main API function for neural architecture search.
    
    Args:
        X: numpy.ndarray (n_samples, timesteps, features) or None
        y: numpy.ndarray One-hot encoded labels or None
        scoring: Metric to optimize ('accuracy')
        data_dir: Path to data if X/y not provided
        **kwargs: Additional optimization parameters
    """

    if population_size < 3:
        raise ValueError("population_size must be at least 3 for evolution")
    
    if len(X) < 5:  # Minimum samples for meaningful evolution
        raise ValueError("Need at least 5 samples for evolution")

    if X is None or y is None:
        from ._data_handler import DataHandler
        handler = DataHandler(data_dir)
        handler.load_and_preprocess()
        X = handler.X_analysis
        y = handler.y_analysis
    
    validate_inputs(X, y)
    
    optimizer = NASOptimizer(scoring=scoring, **kwargs)
    return optimizer.optimize(X, y)