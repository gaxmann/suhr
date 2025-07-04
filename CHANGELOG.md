# Changelog
All notable changes to this project will be documented in this file (tags: Added, Changed, Deprecated, Removed, Fixed, Security).

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.21-public] - 2025-07-04

### Fixed
- Fixed error with "unknown language"(!),

## [2.20] - 2025-07-04

### Added
- Added daylight data
- Added design Telescope 2,
- Introduced date abbreviations due to Chinese,

### Changed
- Changed navigation buttons,
- 'NoneType' object has no attribute 'width' fixed,

## [2.19] - 2025-07-03

### Added
- Added Chinese,

### Changed
- Reduced Gradle dependencies(!),
- Changed navigation buttons,
- Changed order of designs,
- lang_create creates lang_cont from lang directory,
- androidapi 35,
- Adjusted LocationManager,

## [2.18-public] - 2025-06-29

### Added
- Added display of past new moon
- Added OSM email

### Changed
- Brightened telescope moon shadow
- Colored below-horizon area in telescope view

## [2.16] - 2025-06-26

### Added
- Added French
- Added language selector

### Changed
- Changed size ratio in telescope
- Darker gray for below-horizon area in telescope

## [2.15-public] - 2025-06-24

### Added/Removed
- Cleaned up designs (added Telescope in DE, removed test designs)

### Fixed
- Time zone might not have been saved

## [2.14] - 2025-06-23

### Added
- Added design selector (with test designs)
- Error messages are reported

### Changed
- Texts retranslated
- New logo

### Fixed
- Occasionally fixed error when saving settings

## [2.13] - 2025-06-18

### Added
- Added Mercury
- Added E/W in horizon view
- Planet brightness replaces planet size

### Changed
- Moon shadow was slightly too large

### Removed
- Removed ISS

## [2.12] - 2025-06-16

### Added
- Added option “Draw objects larger”
- Added planet sizes in “More details”
- Added ISS

### Changed
- Faster redrawing of dial with same coordinates
- Accelerated location queries (caching)

## [2.11] - 2025-06-14

### Added
- Added “More details” section

### Changed
- Split text across three pages due to rendering issues

## [2.10] - 2025-06-12

### Changed
- Preliminary sketch even faster on slow devices

### Fixed
- GPS note font corrected

## [2.9] - 2025-06-11

### Fixed
- Help was not rendered
- Local sun data deleted after update

## [2.8] - 2025-06-11

### Added
- Now starts faster (shows preview until all calculations are done)
- Introduced third page due to occasional layout errors with flowing text

### Changed
- Sun was too big/small on different devices

### Fixed
- Moon structure was 1 pixel too small

## [2.7] - 2025-06-09

### Changed
- “More margin” now also moves texts
- Changed font

### Fixed
- Moon tick marks were partly flipped
- Missing digital time corrected

## [2.6] - 2025-06-08

### Fixed
- “More margin” now works at startup
- Moon shadow was 1 pixel too small

## [2.5] - 2025-06-07

### Added
- Added “View direction” setting for fixed direction
- Added “More margin” setting for borderless devices

### Changed
- Texts updated

## [2.4] - 2025-06-06

### Changed
- Texts updated

### Fixed
- Moon structure 1 pixel too large

## [2.3] - 2025-06-05

### Changed
- Improved left-right swipe detection
- Brighter moon circle
- Texts updated
- Improved clock_timing

### Fixed
- Settings were overwritten during update

## [2.2] - 2025-06-04

### Changed
- Improved text formatting

### Fixed
- Color scheme flickered

## [2.1] - 2025-06-03

### Added
- Added OSM place search for GPS coordinates, display on dial

### Changed
- Checkboxes more visible

### Fixed
- Saving auto-GPS setting did not work

## [2.0] - 2025-06-01

### Added
- First release of Android version
- Added sun and moon circles
- Added horizon, altitude lines, time markers

## [alpha.0.1 - alpha.0.7] - 2025-05-21..2025-06-01

### Added
- Framework created
- Created 2 pages (dial, settings)
- Time display
- Added sun, moon, and Sirius
- Added GPS query

## [1.0] - 2019-11

### Added
- First version on Raspberry Pi
