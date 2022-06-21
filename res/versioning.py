# generates a version data file that will be read by pyinstaller
import pyinstaller_versionfile
import sys
import os
import re

# TODO move this to the do-it scripts

# this file contains the actual version, generated by setuptools_scm
mymodule_dir = os.path.join(os.path.dirname( __file__ ), '..')
sys.path.append(mymodule_dir)
from src.execution._version import version

# setuptools produces a version like '0.1.dev185+345'
# pyinstaller requires the version be numeric only
print(version)
intermediate = (re.sub(r'[\+]', '.', version.lower())).__str__()
numeric_version = (re.sub(r'[a-z+]', '', intermediate.lower())).__str__()
print(numeric_version)

output_file = os.path.join(mymodule_dir, "versionfile.txt")
print(output_file)
input_file = os.path.join(mymodule_dir, 'res', "metadata.yml")
pyinstaller_versionfile.create_versionfile_from_input_file(
    output_file, input_file,
    # optional, can be set to overwrite version information (equivalent to --version when using the CLI)
    version=numeric_version
)
