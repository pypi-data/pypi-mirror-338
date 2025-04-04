# Changelog

## [0.1.12] - 2024-04-04

### Added
- New `verify_page_load` method in controller for robust page load verification
- Automatic page reload and retry mechanism when elements are not found
- Improved page load waiting with DOM content, network idle, and readyState checks

### Changed
- Removed specific `handle_login` method in favor of more generic page load verification
- Enhanced error handling and retry logic for better reliability
- Updated page load verification to handle dynamic content loading

### Fixed
- Issue with elements not appearing after login without manual page reload
- Improved stability of automated browser interactions
- Better handling of ServiceNow-specific page load requirements 