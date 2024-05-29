import sys
from enum import Enum
import pdb

file_path = 'testpubspec.yaml'

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
                lines[i] = 'version: ' + version_number

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
    return


def parse_args() -> Version:
    if len(sys.argv) < 2: 
        version_type = version_default
    else:
        match sys.argv[1].lower():
            case 'major':
                version_type = Version.MAJOR
            case 'minor':
                version_type = Version.MINOR
            case 'patch':
                version_type = Version.PATCH
            case 'build':
                version_type = Version.BUILD
            case _:
                version_type = Version.BUILD



version_type = parse_args()
update_version_number(version_type)
build_appbundle()
