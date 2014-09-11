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
js_path = partial(os.path.join, parent, JS_PATH)
py_path = partial(os.path.join, parent, PY_PATH)

# Append mpconstants folder to path.
sys.path.append(os.path.join(parent, PY_PATH))


def name(filename):
    return os.path.splitext(os.path.split(filename)[-1])[0]


def names(files):
    return [name(f) for f in files]


def get_json():
    """
    Generate the JSON from the Python files.
    """
    py_files = glob.glob(py_path('*.py'))
    for filename in py_files:
        if filename == 'mozilla_languages':
            raise ValueError('The file mozilla_languages is reserved.')

        mod = importlib.import_module(name(filename))

        export = {}
        for k, v in mod.__dict__.items():
            if k.startswith('__') and k.endswith('__'):
                continue
            export[k] = v

        if not export:
            continue

        output = js_path(filename + '.json')
        change = 'Updating' if os.path.exists(output) else 'Creating'
        print '{0} file: {1}'.format(change, output)
        json.dump(export, open(output, 'w'), indent=2)


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
    get_json()
    get_regions()
    get_languages()
