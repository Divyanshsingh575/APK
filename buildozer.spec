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

    - name: Install Android SDK Build-Tools
      run: |
        # Install Android SDK command-line tools
        sudo apt-get update
        sudo apt-get install -y wget unzip
        wget https://dl.google.com/android/repository/commandlinetools-linux-9333951_latest.zip
        unzip commandlinetools-linux-9333951_latest.zip -d $HOME/.buildozer/android
        rm commandlinetools-linux-9333951_latest.zip
        export ANDROID_HOME=$HOME/.buildozer/android
        export PATH=$ANDROID_HOME/cmdline-tools/tools/bin:$ANDROID_HOME/platform-tools:$PATH
        # Accept licenses and install necessary components
        yes | sdkmanager --licenses
        sdkmanager "platforms;android-33" "build-tools;34.0.0" "platform-tools"

    - name: Build with Buildozer
      run: |
        buildozer android debug
