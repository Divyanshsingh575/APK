[app]
# (str) Title of your application
title = TicTacToe

# (str) Package name
package.name = tictactoe

# (str) Package domain (unique to you, e.g. org.myname)
package.domain = org.divyansh

# (str) Source code where your main.py is located
source.dir = .

# (str) Application entry point
source.entry_point = main.py

# (str) Application version
version = 1.0

# (str) Supported orientation (one of landscape, portrait, all)
orientation = portrait

# (list) Permissions required by the app
android.permissions = INTERNET

# (bool) Fullscreen mode
fullscreen = 1

# (list) List of requirements
requirements = python3, kivy, https://github.com/kivymd/KivyMD/archive/refs/tags/1.1.1.zip, pillow

# (str) Supported architectures
android.arch = arm64-v8a, armeabi-v7a

# (str) The NDK API version to use
android.ndk_api = 23

# (str) Android API version to target
android.api = 31

# (str) Package the app as a release version (disable debug tools)
release = 0

# (bool) Copy all libs instead of stripping them
android.copy_libs = 1

# (bool) Enable debug mode
debug = 1

# (str) Bootstrap to use for build
android.bootstrap = sdl2

# (bool) Whether to include the debug symbols
android.debug_symbols = 0

# (str) Icon file
#icon.filename = icon.png

# (list) Additional Java .jar or .aar libraries to include
android.add_jars =

# (str) Path to additional gradle dependencies
android.gradle_dependencies =

# (str) Keystore information for release
# Leave blank if testing debug builds
android.keystore = debug.keystore
android.keyalias = mykey
android.keypassword = mypassword
android.keystore_password = mypassword

# (str) Package data
# Files from this folder will be included in the APK
package.data = data

# (list) Local Java classes to include
android.local_classes =

# (str) Log level for verbose logs (debug, info, warning, error)
log_level = 2

# (bool) Automatically clean the project before building
clean = 1

# (bool) Allow custom build scripts to be included
android.custombuild = 0
