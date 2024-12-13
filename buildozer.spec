[app]

# (str) Title of your application
title = MyApplication

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) Application version
version = 1.0.0

# (list) Supported orientations
orientation = portrait

# (str) Application icon
icon.filename = %(source.dir)s/assets/icon.png

# (str) Supported platforms
# Uncomment "android" and comment others if targeting only Android
# android -> Generate APK/Bundle, ios -> iOS app, etc.
platforms = android

# (str) Full Python version
python.version = 3.10

# (list) List of Python modules to install using pip
requirements = python3,kivy==2.0.0,pillow

# (str) Entry point of your application
source.main = main.py

# (str) Presplash screen
presplash.filename = %(source.dir)s/assets/splash.png

# (str) Custom Java class package
android.p4a_dir = ./p4a

# (str) Directory where the APK will be saved
android.dist_dir = ./bin

# (bool) Automatically accept Android SDK licenses
android.accept_sdk_license = True

# (str) Android SDK API level
android.sdk_api = 33

# (str) Android build tools version
android.build_tools_version = 34.0.0

# (list) Permissions required for the app
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (bool) Indicate whether the app should use a custom Android Manifest file
# Uncomment if needed
# android.manifest = ./AndroidManifest.tmpl.xml

# (str) Minimum supported Android API level
android.minapi = 21

# (str) Android NDK API level
android.ndk_api = 21

# (str) Architecture target
# Supported: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = arm64-v8a

# (bool) Enable packaging the app as a Bundle (AAB) instead of APK
android.bundle = False

# (str) Application category
# android.category = Games

# (bool) Whether to package additional files
# android.add_assets = True

# (bool) Enable debugging mode
android.debug = True

# (str) Android logcat filter
android.logcat_filters = *:S python:D

# (str) Screenshots directory
android.screenshots = ./screenshots
