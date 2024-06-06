# The Flutter Deploy Tool

## Requirements
The scripts in this repository require at least Python version 3.10 as they use match-case statements.

## Installation
Install by cloning this repository to a location of your choice `git clone https://github.com/friedrich-eibl/flutter_deploy_tool.git`. If it is not in the project folder of where you want to use it, you will have to adjust the according line in the .env file.

Alternatively the Installation is also possible via pip package manager.

## Setup
1. Create a service account in the GoogleCloud Console in order to be able to use the Google Play Developer API.

2. Add a .env file containing the following Values:

```dotenv
PUB_SPEC_PATH = '<path to pubspec.yaml in project>'

KEY_FILE = '<Path to Keyfile for Google Cloud Console>'
PACKAGE_NAME = '<app package name>'
BUNDLE = '<app bundle name>'
```

## Usage
If you want to build and deploy your flutter project with just one command execute 
`python build_and_deploy.py` and follow the instructions in the terminal.

If you only want to build an appbundle for testing without deploying it to your users via the playstore use:

`python build.py [version-type]`


If you only want to automatically publish an already build app-bundle to the Google Play Store you can run this command (this also works for any non-flutter applications):

`python deploy.py`
