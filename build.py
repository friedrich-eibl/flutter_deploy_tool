import sys
import os
from dotenv import load_dotenv
from enum import Enum
import pdb


load_dotenv()
file_path = os.environ['PUB_SPEC_PATH']

Version = Enum('Version', ['MAJOR', 'MINOR', 'PATCH', 'BUILD'])
version_default = Version.BUILD

def get_version() -> str:
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('version:'):
                    return line.split(":")[1].strip()
    except Exception as e:
        print(f'Error getting Version: {e}')
    return 'NULL'


def increment_version(old_version_number: str, version_type: Version) -> str:
    major = int(old_version_number.split(".")[0])
    minor = int(old_version_number.split(".")[1])
    pnb   = old_version_number.split(".")[2].split("+")[0]
    patch = int(pnb[:-1])
    build = int(pnb[-1])
    vcode = int(old_version_number.split("+")[1])
    
    match version_type:
        case Version.MAJOR:
            major += 1
            minor = 0
            patch = 0
            build = 0
        case Version.MINOR:
            minor += 1
            patch = 0
            build = 0
        case Version.PATCH:
            patch += 1
            build = 0
        case Version.BUILD:
            build += 1

    vcode += 1
   
    return str(major) + '.' + str(minor) + '.' + str(patch) + str(build) + '+' + str(vcode)


def set_version(version_number: str):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith('version:'):
                lines[i] = 'version: ' + version_number + '\n'

        with open(file_path, 'w') as file:
            file.writelines(lines)

    except Exception as e:
        print(f'Error setting Version: {e}') 


def update_version_number(version_type: str):
    old_version_number = get_version()
    new_version_number = increment_version(old_version_number, version_type)
    
    set_version(new_version_number)

    print(f'Updated version in pubspec.yaml: {old_version_number} --> {new_version_number}')


def build_appbundle ():
    try:
        if '/' in file_path:
            root = file_path[:file_path.rfind('/')]
            os.system(f'cd {root} && flutter build appbundle')
            return
        os.system('flutter build appbundle')
    except Exception as e:
        print(f'Error building appbundle: {e}')


def parse_args() -> Version:
    if len(sys.argv) < 2: 
        return version_default
    else:
        match sys.argv[1].lower():
            case 'major':
                return Version.MAJOR
            case 'minor':
                return Version.MINOR
            case 'patch':
                return Version.PATCH
            case 'build':
                return Version.BUILD
            case _:
                return Version.BUILD



version_type = parse_args()
update_version_number(version_type)
build_appbundle()
