import re
import sys

PROJECT_REGEX = r'^[-a-zA-Z][-a-zA-Z0-9]+$'
project_name = '{{ cookiecutter.project_name }}'

if not re.match(PROJECT_REGEX, project_name):
    print('ERROR: %s is not a valid Python project name!' % project_name)

    # exits with status 1 to indicate failure
    sys.exit(1)

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{ cookiecutter.module_name }}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: %s is not a valid Python module name!' % module_name)

    # exits with status 1 to indicate failure
    sys.exit(1)