# Kivy Prototype – Historical Reference

**This is an archived PROTOTYPE v2.0.0-alpha.0.1 from 2025. This is NOT part of the current Sun Clock code**

## What is this?

This folder contains the very first working proof-of-concept of Sun Clock as a mobile Kivy application. It demonstrates:
- Basic Kivy app structure
- Two (strangely) rotating visual elements around a digital clock display (Sun and Sirius)
- Buildozer configuration for Android apk building

## Why is it here?

This prototype serves as a **reference for developers** interested in:
- How to structure a Kivy project
- Setting up Buildozer for Android builds
- Understanding early development iterations

## What's NOT in this prototype?

- ❌ NO display of a meaningful sun position
- ❌ NO single-hand clock design
- ❌ NOT the CURRENT Sun Clock concept

## How to run this prototype?

- Install all modules: `pip(3) install kivy pyjnius pillow pytz skyfield numpy jplephem sgp4 olefile`
- Download de421.bsp and put it in the same directory (e.g. from [here](https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/a_old_versions/de421.bsp))
- Download DejaVuSans.ttf and put it in the same directory
- Run the programme with: `python(3) main.py`

---

## The REAL Sun Clock

The **current production version (V2+)** is available at:
- **[Play Store](https://play.google.com/store/apps/details?id=de.ax12.zunclock)**
- **[GitHub Releases](https://github.com/gaxmann/suhr/releases)** (apk downloads)

For questions about the actual Sun Clock, please refer to **the main [README](https://github.com/gaxmann/suhr/tree/main)**
