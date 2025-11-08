[app]
title = ELBASHA Multi Tools
package.name = elbashatools
package.domain = com.elbasha
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy==2.1.0,kivymd==1.1.1,pillow

orientation = portrait

android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25c
android.archs = armeabi-v7a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
