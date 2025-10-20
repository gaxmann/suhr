# Kivy Prototype – Historical Reference

**This is an archived PROTOTYPE (v2.0.0-alpha.0.1, May 2025) and is NOT part of the current Sun Clock codebase.**

## What is this?

This folder contains the very first working proof-of-concept of Sun Clock as a mobile Kivy application. It demonstrates:
- Basic Kivy app structure
- Two rotating visual elements around a digital clock display (Sun and Sirius)
- Buildozer configuration for Android apk building

## Why is it here?

This prototype serves as a reference for developers interested in:
- How to structure a basic Kivy project
- Setting up Buildozer for Android builds
- Understanding early development iterations

## What's NOT in this prototype?

- ❌ No meaningful Sun position display
- ❌ No single-hand clock design
- ❌ Not the current Sun Clock concept in its full form

## How to run this prototype

1. Install all modules: `pip(3) install buildozer kivy pyjnius plyer pillow pytz skyfield numpy jplephem sgp4`
2. Download `de421.bsp` (e.g. from [here](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/a_old_versions/de421.bsp)) and place it in the same directory
3. Download `DejaVuSans.ttf` and place it in the same directory
4. Run with: `python(3) main.py`

---

## The CURRENT Sun Clock

The current production version (V2+) is available at:
- **[Play Store](https://play.google.com/store/apps/details?id=de.ax12.zunclock)**
- **[GitHub Releases](https://github.com/gaxmann/suhr/releases)** (apk downloads)

For questions about the current Sun Clock, please refer to the **[main README](https://github.com/gaxmann/suhr/tree/main)**
