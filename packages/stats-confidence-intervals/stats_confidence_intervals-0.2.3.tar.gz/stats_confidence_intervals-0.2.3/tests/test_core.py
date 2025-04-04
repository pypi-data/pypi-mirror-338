import pytest
import numpy as np
from stats_confidence_intervals.core import (
    mean_confidence_interval,
    proportion_confidence_interval,
    ConfidenceInterval,
    validate_confidence_level,
    validate_data
)

def test_validate_confidence_level():
    """Test confidence level validation."""
    with pytest.raises(ValueError):
        validate_confidence_level(0)
    with pytest.raises(ValueError):
        validate_confidence_level(1)
    with pytest.raises(ValueError):
        validate_confidence_level(-0.5)
    with pytest.raises(ValueError):
        validate_confidence_level(1.5)
    # This should not raise an error
    validate_confidence_level(0.95)

def test_validate_data():
    """Test data validation."""
    with pytest.raises(ValueError):
        validate_data([])
    with pytest.raises(ValueError):
        validate_data(['a', 'b', 'c'])
    # These should not raise errors
    validate_data([1, 2, 3])
    validate_data([1.5, 2.5, 3.5])

def test_mean_confidence_interval():
    """Test mean confidence interval calculation."""
    data = [1, 2, 3, 4, 5]
    ci = mean_confidence_interval(data)
    
    assert isinstance(ci, ConfidenceInterval)
    assert pytest.approx(ci.estimate) == 3.0
    assert ci.lower_bound < ci.estimate
    assert ci.upper_bound > ci.estimate
    assert ci.confidence_level == 0.95

    # Test with different confidence level
    ci_90 = mean_confidence_interval(data, confidence=0.90)
    assert ci_90.confidence_level == 0.90
    # 90% CI should be narrower than 95% CI
    assert ci_90.lower_bound > ci.lower_bound
    assert ci_90.upper_bound < ci.upper_bound

def test_proportion_confidence_interval():
    """Test proportion confidence interval calculation."""
    # Test with Wilson method
    ci_wilson = proportion_confidence_interval(7, 10, method='wilson')
    assert isinstance(ci_wilson, ConfidenceInterval)
    assert pytest.approx(ci_wilson.estimate) == 0.7
    assert ci_wilson.lower_bound < ci_wilson.estimate
    assert ci_wilson.upper_bound > ci_wilson.estimate

    # Test with normal approximation method
    ci_normal = proportion_confidence_interval(7, 10, method='normal')
    assert isinstance(ci_normal, ConfidenceInterval)
    assert pytest.approx(ci_normal.estimate) == 0.7

    # Test invalid inputs
    with pytest.raises(ValueError):
        proportion_confidence_interval(11, 10)  # successes > total
    with pytest.raises(ValueError):
        proportion_confidence_interval(5, 0)    # total <= 0
    with pytest.raises(ValueError):
        proportion_confidence_interval(5, 10, method='invalid')  # invalid method
