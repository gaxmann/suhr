[app]
title = Sonnenuhr
package.name = sunclock
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,bsp
source.exclude_dirs = __UNUSED, code
version = 0.1
requirements = python3,kivy,plyer,pillow,skyfield,pytz,cython==0.29.33
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION
android.api = 34
android.minapi = 21
android.icon = icons/play_store_512.png
osx.python_version = 3
osx.kivy_version = 1.9.1
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
