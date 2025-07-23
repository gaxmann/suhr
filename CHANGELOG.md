# Changelog
All notable changes to this project will be documented in this file (tags: Added, Changed, Deprecated, Removed, Fixed, Security).

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.34] - 2025-07-24

### Added
- Agnihotra lines on dial added,
 
## [2.33-public] - 2025-07-22 (Atmospheric refraction)

### Fixed
- Android 7-12 "1x Location" error fixed

## [2.32] - 2025-07-21

### Added
- Button "1x location" added
- Popup support added
- On error report show return text
  
## [2.31] - 2025-07-20

### Changed
- Altitude and temperature added to location
- standard design now is telescope
- Errors fixed

## [2.30] - 2025-07-19

### Changed
- location update improved,
- Update button also updates location,
- "Display Agnihotra" use GPS instead of network for more location accuracy
- min. API now 23

## [2.29] - 2025-07-18

### Fixed
- Dial wasnt properly deleted before recreation, 

### Changed
- White window fix Window.update_viewport,
- Improved location request, 

## [2.27/28] - 2025-07-17

### Changed
- Painting of dial sped up (only one file),
- Update button also creates new background img,
- Location can now also be retrieved from GPS module 

## [2.26] - 2025-07-15

### Added
- Atmospheric refraction activated, 
- Adaptive resolution of orbits introduced,

### Fixed
- Remove spaces from place names

### Changed
- Update button now also retrieves GPS (if active),

## [2.25-public] - 2025-07-11 (Agnihotra times)

### Fixed
- Key error fixed,

## [2.24] - 2025-07-11

### Fixed
- Error with Clock.schedule_once fixed (important!),

### Added
- "Display Agnihotra time on dial" option added, 
- Fifth page added with local data,

### Changed
- Swipe class improved (to not interfere with zoom),
- Language switcher now in local tongue,
- Texts updated
- Agnihotra calculation accelerated

## [2.23] - 2025-07-08

### Added
- Dropdown lists now also change language
- Sky image now zoomable

## [2.22] - 2025-07-06

### Fixed
- Time zone could not be changed manually
- 'NoneType' object has no attribute 'bind'

### Changed
- Upgraded to Cython 3.0.11
  
### Added/Removed
- Daylight info was replaced by Agnihotra time
- Chinese date formatting added

## [2.21-public] - 2025-07-04 (Chinese language)

### Fixed
- (!)"Unknown language" error fixed,

## [2.20] - 2025-07-04

### Fixed
- 'NoneType' object has no attribute 'width' fixed,

### Added
- Daylight data added
- Design "Telescope 2" added,
- Date abbreviations introduced due to Chinese,

### Changed
- Navigation buttons changed,

## [2.19] - 2025-07-03

### Added
- Chinese added,

### Changed
- (!)Gradle dependencies reduced,
- Navigation buttons changed,
- Order of designs changed,
- lang_create creates lang_cont from lang directory,
- Upgraded to Android api 35,
- Adjusted LocationManager,

## [2.17/18-public] - 2025-06-29 (Teleskop design)

### Added
- Time of past new moon displayed
- OSM email address added

### Changed
- Telescope moon shadow brightened 
- Below-horizon area in telescope view colored 

## [2.16] - 2025-06-26

### Added
- French added
- Language selector added

### Changed
- Size ratio in telescope changed
- Darker gray for below-horizon area in telescope

## [2.15-public] - 2025-06-24 (First public version)

### Added/Removed
- Designs cleaned up (added Telescope in 'de', removed test designs)

### Fixed
- Timezone might not have been saved

## [2.14] - 2025-06-23

### Added
- Design selector added (with test designs)
- Error messages are now reported

### Changed
- Texts newly translated
- New logo added

### Fixed
- Fixed occasional error when saving settings

## [2.13] - 2025-06-18

### Added
- Mercury added
- E/W added in horizon view
- Planet brightness replaces planet size

### Changed
- Moon shadow was slightly too large

### Removed
- ISS removed 

## [2.12] - 2025-06-16

### Added
- Added option “Draw objects larger”
- Added planet sizes in “More details”
- ISS added

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
- Added OSM place search for GPS coordinates, display on dial (only for newer machines)

### Changed
- Checkboxes more visible

### Fixed
- Saving auto-GPS setting did not work

## [2.0] - 2025-06-01

### Added
- First release of Android version
- Added sun and moon circles
- Added horizon, altitude lines, time markers

## [2.alpha.1 - 2.alpha.7] - 2025-05-21..2025-06-01

### Added
- Framework created
- Created 2 pages (dial, settings)
- Time display
- Added sun, moon, and Sirius
- Added GPS query

## [1.0] - 2019-11

### Added
- First version on Raspberry Pi
