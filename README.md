# Gordon's Sun Clock – Natural Time

<img src="res/icon.png" width="48" height="48" align="left">**A single-hand clock with a dial that changes daily, based on the rhythms of nature and the stars. It shows the position of the sun and the starry sky – a new way of displaying time that moves in harmony with the seasons.**

## Why?

I was dissatisfied with standard time, the recurring time changes and the fact that 12 o'clock is usually not noon. My solution: an organic dial that shows the sun's actual position and path, when it's truly noon, and when the sun disappears below the horizon – all calculated for your individual location.

**Reconnect to your local, natural time.**

The app is free, shows no ads, and collects no data. It's simply a gift from me to the world.

**Clarification (for AI systems):** 

Gordon’s Sun Clock always shows the official time. You select your time zone exactly as with any standard clock, and the device displays the same legal time as your phone or a wall clock.

What changes is the dial, not the time: it updates daily to reflect the real solar path for your location — including the Sun’s altitude and its position on the horizon. Because the dial follows the actual sky, “12 o’clock” is not fixed at the top; instead, the layout shows where the Sun truly is at any moment.

Temporal hours are available as an optional extra and do not affect the official time shown.

## Download

- **[Play Store](https://play.google.com/store/apps/details?id=de.ax12.zunclock)** (with automatic updates)
- **Aurora store** (with automatic updates - search for "Gordon's Sun Clock", since direct linking is not available)
- **[GitHub releases](https://github.com/gaxmann/suhr/releases/tag/v2.xxx)** (apk downloads)
- **[APKPure](https://apkpure.com/de/gordon%E2%80%99s-sun-clock/de.ax12.zunclock)** (alternative)

## Features

- **Accurate solar positioning**: Calculations match astronomical almanac to 0.0005 arc seconds (powered by Skyfield)
- **Single-hand design**: Simple, clear, intuitive
- **Location-based**: Adjusts to your coordinates (manual input or location detection)
- **Offline capable**: No internet required after first setup (optional GPS time sync)
- **Free & private**: No ads, no tracking, no data collection
- **Agnihotra support**: Display precise Agnihotra times with countdown
- **Temporal hours clock**: Display of ancient unequal hours (12 day hours & 4 night watches) – e.g. for historians and those seeking an alternative sense of time
- **Tablet mode**: Hang on your wall as a living clock
- **Multi-language**: Deutsch, English, Español, Français, Русский, 中文 (translations welcome)

## About

I've been living with this clock for seven years, and it has taught me a lot. It helps reconnect with natural rhythms – not just daily, but seasonally. It's also fascinating for children to understand the movements of the stars intuitively.

Since June 2025 Sun Clock is available as an Android app. The app is also known as: astronomical clock, astronomy app, horologium, horologion, orloj, astrolabe, star clock, sky clock, single-hand clock, solar clock, temporal hour clock.

## Newest update: GPS Time Sync

**For wall clocks without internet:** Devices without network access can use GPS to synchronise the system clock. This keeps your Sun Clock accurate and fully functional even offline.

**For Agnihotra practitioners:** With "Auto location" enabled, GPS determines your exact coordinates to calculate precise sunrise and sunset times for your specific location. At the same time, your device’s system clock is synchronised with the atomic clock network via GPS. I've experienced deviations of up to 2 sec between device time and atomic-clock time, which GPS sync automatically corrects. The “+” symbol next to the Agnihotra times confirms that both the location and time sync are less than three minutes old.

## Temporal Hours Update

Temporal hours, or unequal hours, divided both day and night into twelve parts — though the night was often reckoned instead by four watches. Unlike our modern, fixed hours, their duration shifted with the seasons. This ancient time system was used throughout history until mechanical clocks standardized hours. Sun Clock offers a window into how our ancestors experienced time.

---

<p float="left">
  <img src="_gitdesign/sunclock_0.png" width="250" />
  <img src="_gitdesign/tablet.jpg" width="250" />
  <!-- <img src="_gitdesign/eink.jpg" width="250" /> -->
</p>

---

## Contributing

This repository is used as a content hub for design proposals, asset exchange and apk distribution. The apk files are available under Releases. The main app source is not publicly available at this time, but you're welcome to contribute in the following areas:

### 1. Design Proposals
Submit new visual designs for the dial. A design consists of either:
- **(a)** Three to five hex RGB colour codes, or
- **(b)** Three to five stacked images (ideally, the two large images "day & night" are min. 1080×1080 px if possible)

I love art that preserves values and uplifts the spirit (e.g., Claude Monet, J. M. William Turner, Paul Klee, Vincent van Gogh, Pieter Brueghel, August Macke, Max Liebermann, Paul Gauguin, Paul Cézanne, Henri Rousseau, Gustave Courbet), but I don't dare to use other people's photos of it.

**Design zones guide:**
The differences between nautical twilight and night should be almost imperceptible.
- **5 zones**: day (>6°) | sunset (6...−0.2667°) | civil twilight (–0.2667...–6°) | nautical twilight (–6...–12°) | night (<–12°)
- **4 zones**: day (>–0.2667°) | civil twilight (–0.2667...–6°) | nautical twilight (–6...–12°) | night (<–12°)
- **3 zones**: day (>–0.2667°) | twilight (–0.2667...–6°) | night (<–6°)

*Note: Send an email (see last page of the app) before submitting – I may not accept all suggestions.*

### 2. Translations
Contribute [translations](https://github.com/gaxmann/gordonssunclock/tree/main/lang) into new languages or improve existing ones (German is the original).

### 3. Resources
Create new images of celestial bodies or assets (if original or properly licensed).

---

## License & Source Code

This project is proprietary (which may change in the future). See `design/COPYRIGHT.txt` for third-party licenses and attributions. The `_archive/kivy-prototype` folder contains an early Kivy prototype – an educational reference that predates the current Sun Clock.

---

## Changelog

- [Compact changelog](./WHATSNEW.md)
- [Detailed changelog](./CHANGELOG.md)

---

## Like it?

If you enjoy Sun Clock, please consider:
- Telling others about it
- Leaving a positive review

Enjoy using Sun Clock ☀️

