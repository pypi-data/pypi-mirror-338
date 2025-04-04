# Changelog

## [0.2.3] - 2024-04-03
### Added
- Automated GitHub release workflow
- Automated PyPI publishing workflow
- Comprehensive test workflow for multiple Python versions (3.8-3.12)
- Improved CI/CD pipeline with automated testing and deployment

### Changed
- Updated project structure for better automation
- Enhanced release process with automatic changelog integration
- Improved test coverage across multiple Python versions

## [0.2.2] - 2024-04-03
### Added
- Implemented custom Wilson score interval method for better proportion confidence intervals
- Added custom normal approximation interval method
- Improved reliability by removing dependency on scipy.stats.proportion_confint

## [0.2.1] - 2024-04-03

### Changed
- Renamed package from Stats_CI to confidence_interval for better clarity
- Updated package metadata and documentation
- Implemented custom Wilson score and normal approximation methods for proportion confidence intervals
- Removed dependency on scipy.stats.proportion_confint

## [0.2.0] - 2024-04-03

### Added
- Added proportion confidence intervals with Wilson score and normal approximation methods
- Added visualization capabilities with matplotlib
- Added input validation and error handling
- Added type hints for better IDE support
- Added comprehensive test suite
- Added example script using California housing dataset

### Changed
- Improved package structure
- Updated documentation
- Enhanced error messages
- Added proper return types using ConfidenceInterval class

## [0.1.2] - 2024-04-03

### Added
- Initial release with mean confidence intervals
- Basic documentation
- Simple test suite 