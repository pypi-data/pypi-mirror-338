import scipy.stats as stats
import numpy as np
from typing import List, Tuple, Union, Optional
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class ConfidenceInterval:
    """Class to hold confidence interval results."""
    estimate: float
    lower_bound: float
    upper_bound: float
    confidence_level: float

def validate_confidence_level(confidence: float) -> None:
    """Validate that the confidence level is between 0 and 1."""
    if not 0 < confidence < 1:
        raise ValueError("Confidence level must be between 0 and 1")

def validate_data(data: Union[List[Union[int, float]], np.ndarray]) -> None:
    """Validate input data."""
    if isinstance(data, list):
        if not data:
            raise ValueError("Data cannot be empty")
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("All data must be numeric")
    elif isinstance(data, np.ndarray):
        if data.size == 0:
            raise ValueError("Data cannot be empty")
        if not np.issubdtype(data.dtype, np.number):
            raise ValueError("All data must be numeric")
    else:
        raise ValueError("Data must be a list or numpy array")

def mean_confidence_interval(
    data: Union[List[Union[int, float]], np.ndarray], 
    confidence: float = 0.95
) -> ConfidenceInterval:
    """
    Calculate confidence interval for the mean of a dataset.
    
    Args:
        data: List of numeric values or numpy array
        confidence: Confidence level (between 0 and 1)
    
    Returns:
        ConfidenceInterval object containing the mean and confidence bounds
    """
    validate_confidence_level(confidence)
    validate_data(data)
    
    a = np.array(data, dtype=float)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = se * stats.t.ppf((1 + confidence) / 2., n-1)
    return ConfidenceInterval(m, m-h, m+h, confidence)

def wilson_score_interval(successes: int, total: int, confidence: float = 0.95) -> Tuple[float, float]:
    """
    Calculate Wilson score interval for a proportion.
    
    Args:
        successes: Number of successes
        total: Total number of trials
        confidence: Confidence level (between 0 and 1)
    
    Returns:
        Tuple of (lower bound, upper bound)
    """
    if total == 0:
        raise ValueError("Total must be positive")
    
    p = float(successes) / total
    z = stats.norm.ppf((1 + confidence) / 2.)
    z2 = z * z
    
    # Calculate terms for Wilson score interval
    denominator = 1 + z2/total
    center = (p + z2/(2*total)) / denominator
    spread = z * np.sqrt(p*(1-p)/total + z2/(4*total*total)) / denominator
    
    return center - spread, center + spread

def normal_approximation_interval(successes: int, total: int, confidence: float = 0.95) -> Tuple[float, float]:
    """
    Calculate normal approximation interval for a proportion.
    
    Args:
        successes: Number of successes
        total: Total number of trials
        confidence: Confidence level (between 0 and 1)
    
    Returns:
        Tuple of (lower bound, upper bound)
    """
    if total == 0:
        raise ValueError("Total must be positive")
    
    p = float(successes) / total
    z = stats.norm.ppf((1 + confidence) / 2.)
    se = np.sqrt(p * (1-p) / total)
    
    return p - z*se, p + z*se

def proportion_confidence_interval(
    successes: int,
    total: int,
    confidence: float = 0.95,
    method: str = 'wilson'
) -> ConfidenceInterval:
    """
    Calculate confidence interval for a proportion.
    
    Args:
        successes: Number of successes
        total: Total number of trials
        confidence: Confidence level (between 0 and 1)
        method: Method to use ('wilson' or 'normal')
    
    Returns:
        ConfidenceInterval object containing the proportion and confidence bounds
    """
    validate_confidence_level(confidence)
    if successes > total:
        raise ValueError("Number of successes cannot exceed total")
    if total <= 0:
        raise ValueError("Total must be positive")
    
    p = successes / total
    
    if method == 'wilson':
        lower, upper = wilson_score_interval(successes, total, confidence)
    elif method == 'normal':
        lower, upper = normal_approximation_interval(successes, total, confidence)
    else:
        raise ValueError("Method must be 'wilson' or 'normal'")
    
    return ConfidenceInterval(p, lower, upper, confidence)

def plot_confidence_interval(
    ci: ConfidenceInterval,
    label: Optional[str] = None,
    create_figure: bool = False,
    y_offset: float = 1.0
) -> None:
    """
    Plot a confidence interval.
    
    Args:
        ci: ConfidenceInterval object
        label: Optional label for the plot
        create_figure: Whether to create a new figure
        y_offset: Y-axis position for the interval (useful for multiple intervals)
    """
    if create_figure:
        plt.figure(figsize=(10, 2))
    
    plt.plot([ci.lower_bound, ci.upper_bound], [y_offset, y_offset], 'b-', linewidth=2)
    plt.plot([ci.estimate], [y_offset], 'ro')
    plt.axvline(x=ci.estimate, color='r', linestyle='--', alpha=0.3)
    
    if create_figure:
        plt.title(f'{ci.confidence_level*100}% Confidence Interval')
        if label:
            plt.xlabel(label)
        plt.grid(True, alpha=0.3)
        plt.show()
