import numpy as np
from collections import deque

class RunningMetrics:
    """
    A class to track running metrics over a window of frames.
    """
    def __init__(self, window_size=30):
        """
        Initialize the metrics tracker.
        
        Args:
            window_size (int): Number of frames to maintain in history
        """
        self.window_size = window_size
        self.metrics = {}
    
    def add_metric(self, name, initial_value=None):
        """
        Add a new metric to track.
        
        Args:
            name (str): Name of the metric
            initial_value: Optional initial value for the metric
        """
        self.metrics[name] = deque(maxlen=self.window_size)
        if initial_value is not None:
            self.metrics[name].append(initial_value)
    
    def update(self, metric_name, value):
        """
        Update a metric with a new value.
        
        Args:
            metric_name (str): Name of the metric to update
            value: New value to add
        """
        if metric_name not in self.metrics:
            raise KeyError(f"Metric name: {metric_name} is not initialized.")
        self.metrics[metric_name].append(value)
    
    def get_average(self, metric_name):
        """
        Get the average value of a metric over its window.
        
        Args:
            metric_name (str): Name of the metric
            
        Returns:
            float: Average value or None if no values exist
        """
        if not self.metrics.get(metric_name):
            return None
        return np.mean(self.metrics[metric_name], axis=0)
    
    def get_min(self, metric_name):
        """Get the minimum value in the window."""
        if not self.metrics.get(metric_name):
            return None
        return np.min(self.metrics[metric_name])
    
    def get_max(self, metric_name):
        """Get the maximum value in the window."""
        if not self.metrics.get(metric_name):
            return None
        return np.max(self.metrics[metric_name])
    
    def get_std(self, metric_name):
        """Get the standard deviation over the window."""
        if not self.metrics.get(metric_name):
            return None
        return np.std(self.metrics[metric_name])
    
    def get_current(self, metric_name):
        """Get the most recent value."""
        if not self.metrics.get(metric_name):
            return None
        return self.metrics[metric_name][-1]
    
    def get_all_values(self, metric_name):
        """Get all values in the current window."""
        return list(self.metrics.get(metric_name, []))
    
    def reset(self, metric_name=None):
        """
        Reset metrics. If metric_name is provided, reset only that metric.
        Otherwise, reset all metrics.
        """
        if metric_name:
            if metric_name in self.metrics:
                self.metrics[metric_name].clear()
        else:
            for metric in self.metrics:
                self.metrics[metric].clear()
    
    def is_metric_added(self, name):
        return name in self.metrics