# Confidence Interval Library

A Python library for calculating and visualizing confidence intervals.

## Installation

```bash
pip install confidence_interval
```

## Features

- Calculate confidence intervals for means
- Calculate confidence intervals for proportions using:
  - Wilson score method (recommended for small sample sizes)
  - Normal approximation method (for large sample sizes)
- Visualize confidence intervals with customizable plots
- Support for both list and numpy array inputs
- Comprehensive error checking and validation

## Usage

### Mean Confidence Interval

```python
from confidence_interval.core import mean_confidence_interval
import numpy as np

data = np.random.normal(100, 15, size=50)
ci = mean_confidence_interval(data, confidence=0.95)
print(f"Mean: {ci.estimate:.2f}")
print(f"95% CI: ({ci.lower_bound:.2f}, {ci.upper_bound:.2f})")
```

### Proportion Confidence Interval

```python
from confidence_interval.core import proportion_confidence_interval

successes = 45
total = 100
ci = proportion_confidence_interval(successes, total, confidence=0.95, method='wilson')
print(f"Proportion: {ci.estimate:.2f}")
print(f"95% CI: ({ci.lower_bound:.2f}, {ci.upper_bound:.2f})")
```

## Development

This project uses GitHub Actions for automated testing and deployment. The workflow includes:

- Automated tests on Python versions 3.8-3.12
- Automatic releases when tags are pushed
- Automated PyPI publishing

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest tests/`)
5. Commit your changes (`git commit -m 'feat: Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Release Process

The release process is automated through GitHub Actions:

1. Update version in `setup.py`
2. Add entry to `CHANGELOG.md`
3. Commit changes
4. Create and push a tag:
   ```bash
   git tag -a v0.x.x -m "Release version 0.x.x"
   git push origin v0.x.x
   ```
5. GitHub Actions will automatically:
   - Create a GitHub release
   - Run tests
   - Publish to PyPI

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.

```

