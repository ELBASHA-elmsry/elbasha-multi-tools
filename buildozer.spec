[app]
title = ELBASHA Multi Tools
package.name = elbashamultitools
package.domain = com.elbasha
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.0

# إصدارات متوافقة مع python-for-android
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a
android.accept_sdk_license = True
android.gradle_dependencies = 

[buildozer]
log_level = 2
warn_on_root = 1
