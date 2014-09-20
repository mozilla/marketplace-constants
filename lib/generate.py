"""
This is a pretty simple and naive script to pull all the data from either:
* the Python scripts
* or the Mozilla SVN server to give us access to contents.

The intent of this script is to run it, let it update any files in git
and then commit the changes on each release.
"""
from functools import partial
import glob
import importlib
import json
import pprint
import os
import re
import sys

import requests


parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set up partials to easily get the path of a JS/PY file.
JS_PATH = 'dist/js'
PY_PATH = 'mpconstants'
LIB_PATH = 'lib'
js_path = partial(os.path.join, parent, JS_PATH)
py_path = partial(os.path.join, parent, PY_PATH)
lib_path = partial(os.path.join, parent, LIB_PATH)

# Append mpconstants folder to path.
sys.path.append(os.path.join(parent, PY_PATH))


def name(filename):
    return os.path.splitext(os.path.split(filename)[-1])[0]


def names(files):
    return [name(f) for f in files]


def get_js_modules():
    """
    Generate JS modules from the Python files.
    """
    js_module_template = open(lib_path('require_template.js'), 'r').read()
    py_files = glob.glob(py_path('*.py'))

    for filename in py_files:
        filename = name(filename)
        if filename == 'mozilla_languages':
            # The file mozilla_languages is reserved.
            continue

        # Get the data.
        mod = importlib.import_module(filename)

        # Build the data.
        data = {}
        for k, v in mod.__dict__.items():
            if k.startswith('__') and k.endswith('__'):
                continue
            data[k] = v
        if not data:
            continue
        data = json.dumps(data).replace("'", "\\'")

        # Write the data.
        output = js_path(filename + '.js')
        change = 'Updating' if os.path.exists(output) else 'Creating'
        print '{0} file: {1}'.format(change, output)
        open(output, 'w').write(js_module_template % data)


def get_languages():
    """
    Generate the languages by reading them from svn and generate the
    matching Python files.
    """
    remote = 'http://svn.mozilla.org/libs/product-details/json/languages.json'
    print 'Fetching: languages'
    data = requests.get(remote)
    (open(js_path('mozilla_languages.json'), 'w')
          .write(json.dumps(data.json(), indent=2)))
    (open(py_path('mozilla_languages.py'), 'w').write(
          u'LANGUAGES = ' + pprint.pformat(data.json())))


def get_regions():
    """
    Generate the regions by reading them from svn and generate the
    matching Python files.
    """
    remote = 'http://svn.mozilla.org/libs/product-details/json/regions/'
    data = requests.get(remote)
    links = set(re.findall(r'href="([^"]+.json)"', data.content))

    for link in sorted(links):
        print 'Fetching: region {0}'.format(link)
        data = requests.get(remote + link)

        js_file = open(js_path('regions/{0}'.format(link)), 'w')
        js_file.write(json.dumps(data.json(), indent=2))

        py_filename = 'regions/{0}'.format(
            link.replace('.json', '.py').replace('-', '_'))
        py_file = open(py_path(py_filename), 'w')
        py_file.write(u'REGIONS = ' + pprint.pformat(data.json()))


if __name__ == '__main__':
    get_js_modules()
    get_regions()
    get_languages()
