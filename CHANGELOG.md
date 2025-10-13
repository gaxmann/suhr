# Changelog
All notable changes to this project will be documented in this file (tags: Added, Changed, Deprecated, Removed, Fixed, Security). The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html). 

[Here](./WHATSNEW.md) you'll find a short summary of the latest changes. Below you'll find [future versions](#dev) of the app (supporting Android 15+ and 16 kb).

## [2.56-public] - 2025-10-13 _(Reunification with Android 5)_

### Changed
- Own creation of android.version_code to be able to revert back to api 21(-35)
- Replacing versiondat with vs.dat (faster, more reliable)
- Restructuring of the settings page
- Reverting to api level 21-35 (Android 5+) to have fewer branches

## [2.54-public] - 2025-10-08

### Changed
- Reverted API level back to 23-35 (Android 6+), restoring previous default, because of kivys automatic version_code system 

### Fixed
- KeyError font10
- Android 15+ bars fixed

## [2.53-android5] - 2025-10-08 (Legacy Support)

### Changed
- Special build (no Play Store) for API 21-34 ([Android 5+](https://github.com/gaxmann/suhr/releases/tag/v2.xxx)) due to the unavoidable, upcoming Android 7+ requirement 

### Fixed
- KeyError font10

## [2.52-public] - 2025-10-06

### Changed
- "Update available" message shown on dial for devices installed via apk (checked quarterly)

### Fixed
- no attribute clock_screen

## [2.51-public] - 2025-10-04

### Changed
- Google doesn't add "com.android.vending.CHECK_LICENSE" any more (alternative store work now, e.g. Aurora, Apkpure)
- Calculation of dial creation time improved
- Size of saturn increased

## [2.50-public] - 2025-10-02/3

### Fixed
- GrapheneOS (app dir not found)

## [2.49-public] - 2025-09-28

### Fixed
- Location string on dial fixed

## [2.48-public] - 2025-09-26

### Added
- Calculates whether the sun moves across the south or north (and adjusts dial accordingly)

### Fixed
- Android 15+ max altitude corrected for bars
- Line spacing on dial fixed

## [2.47-public] - 2025-09-20

### Changed
- Size of bar corrected to dpi

## [2.46-public] - 2025-09-17 (Bar handling)

### Changed
- Error corrections: bars hid content on Android 15+
- Moon image moved to design dir

## [2.45-public] - 2025-09-14

### Changed
- Design Telescope: star symbols smaller
- Error corrections: Agnihotra is None
- Turned moon image 2°

## [2.44-public] - 2025-09-06

### Changed
- Moon shadow 1 pixel too big,
- Smaller center marker,
- Autocenter dial 2 min after start (fullscreen center problem),
- Long text block split (2c/d)

### Fixed
- Errors in text and translation corrected

## [2.43-public] - 2025-09-01 

### Fixed
- Error corrections (update message didnt go away)
- Translation mistakes fixed

### Changed
- Update text is now clickable (leads to Playstore)
- Pages rearranged

## [2.42-public] - 2025-08-29 (Update prompt) 

### Fixed
- Error corrections (update avail. and error handling)

## [2.41] - 2025-08-25 

### Changed
- Display "Update available" on dial on devices that run 24/7 (checks once a week)

## [2.40-public] - 2025-08-21

### Fixed
- Fixed hour figures were printed twice in NZ,
- Popup global error fixed, 

## [2.39-public] - 2025-08-10 (Smaller Database)

### Changed
- Moon border improved

## [2.38] - 2025-08-09

### Changed
- Planet database reduced (til 2040), 

### Fixed
- Window NoneType error fixed,
- Agnihotra line on dial disappeared after midnight,
- Timezonefinder error,

## [2.37-public] - 2025-08-06 (Nicer moon)

### Fixed
- Window error fixed 

## [2.36] - 2025-08-05 

### Changed
- Design Telescope: moon image improved 

## [2.35-public] - 2025-07-30 (Better zoom)

### Fixed
- Location error on Honor fixed,

### Added
- Agnihotra lines on dial added,

### Changed
- Zoom resolution doubled (slower dial creation)
- Triple tap zooms also in
- Telescope design: planet size decreased (pow 0.15->0.24)
- Text creation on dial sped up
- Error corrections: timezonefinder, OSM location
 
## [2.33-public] - 2025-07-22 (Atmospheric refraction)

### Fixed
- Android 7-12 "1x Location" button fixed

## [2.32] - 2025-07-21

### Added
- Button "1x location" added
- Popup support added
- On error report show return text
  
## [2.31] - 2025-07-20

### Changed
- Altitude and temperature added to location
- standard design now is Telescope
- Errors fixed

## [2.30] - 2025-07-19

### Changed
- location update improved,
- Update button also updates location,
- "Display Agnihotra" use GPS instead of network for more location accuracy
- Min. API 23 (Android 6+)

## [2.29] - 2025-07-18

### Fixed
- Dial wasnt properly deleted before recreation, 

### Changed
- White window fix Window.update_viewport,
- Improved location request, 

## [2.27+28] - 2025-07-17

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
- Min. API 24 (Android 7+)

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
- Design Telescope 2 added,
- Date abbreviations introduced due to Chinese,

### Changed
- Navigation buttons changed,

## [2.19] - 2025-07-03

### Added
- Chinese added,

### Changed
- Gradle dependencies reduced
- Navigation buttons changed
- Order of designs changed
- lang_create creates lang_cont from lang directory
- Upgraded to Android api 35 (21-35)
- Adjusted LocationManager

## [2.17/18-public] - 2025-06-29 (Telescope design)

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

## [2.15-public] - 2025-06-24 (Initial publication)

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
- E|W added in horizon view
- Planet brightness replaces planet size

### Changed
- Moon shadow was slightly too large

### Removed
- ISS removed 

## [2.12] - 2025-06-16

### Added
- Added option "Draw objects larger"
- Added planet sizes in "More details"
- ISS added

### Changed
- Faster redrawing of dial with same coordinates
- Accelerated location queries (caching)

## [2.11] - 2025-06-14

### Added
- Added "More details" section

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
- "More margin" now also moves texts
- Changed font

### Fixed
- Moon tick marks were partly flipped
- Missing digital time corrected

## [2.6] - 2025-06-08

### Fixed
- "More margin" now works at startup
- Moon shadow was 1 pixel too small

## [2.5] - 2025-06-07

### Added
- Added "View direction" setting for fixed direction
- Added "More margin" setting for borderless devices

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
- Color scheme flickered between day and night

## [2.1] - 2025-06-03

### Added
- Added OSM place search for GPS coordinates (only for newer machines)
- Displays place on dial

### Changed
- Checkboxes more visible

### Fixed
- Auto-GPS settings did not save

## [2.0] - 2025-06-01

### Changed
- First release of fully functioning Android version (closed testing)

### Added
- Added sun's and moon's orbit ("circles")
- Added horizon, altitude lines, time markers

## [2.0.0-alpha.1 - 2.0.0-alpha.7] - 2025-05-21..2025-06-01

### Added
- Android framework created
- Created pages "dial" and "settings"
- Displays digital time
- Added sun, moon and Sirius
- Added coarse location query
- Min. API 21 (Android 5+)

## [1.0 - 1.73] - 2019-11..2025

### Added
- First version on Raspberry Pi with an e-paper display

---
---
<a name="dev"></a>
## [3.0-dev] - 2025-10-12 (Transparent bars)

### Changed
- Navigation and status bars now transparent on Android 15+
- Slightly slower performance on 4 kB devices
- Includes all features up to version 2.54
- Min. API 24 (Android 7+) and arm64-v8a only, because of 16 kB memory pages and new numpy version 



