name: Build Android APK

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.10"

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install buildozer
        pip install cython kivy

    - name: Install Android SDK
      run: |
        export ANDROID_HOME=$HOME/.buildozer/android/platform/android-sdk
        export PATH=$ANDROID_HOME/tools:$ANDROID_HOME/tools/bin:$ANDROID_HOME/platform-tools:$PATH
        mkdir -p $ANDROID_HOME
        # Install Android SDK Command-line tools
        wget https://dl.google.com/android/repository/commandlinetools-linux-9477386_latest.zip -P $HOME/.buildozer/android/
        unzip $HOME/.buildozer/android/commandlinetools-linux-9477386_latest.zip -d $ANDROID_HOME
        rm $HOME/.buildozer/android/commandlinetools-linux-9477386_latest.zip
        # Accept licenses for Android SDK
        yes | $ANDROID_HOME/cmdline-tools/bin/sdkmanager --licenses
        # Install Android SDK platforms and build-tools
        $ANDROID_HOME/cmdline-tools/bin/sdkmanager "platforms;android-33" "build-tools;34.0.0" "platform-tools"

    - name: Set up Buildozer for Android
      run: |
        buildozer init

    - name: Build APK with Buildozer
      run: |
        buildozer android debug
