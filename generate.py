"""
This is a pretty simple and naive script to pull all the data from either:
* the Python scripts
* or the Mozilla SVN server to give us access to contents.

The intent of this script is to run it, let it update any files in git
and then commit the changes on each release.
"""
import glob
import importlib
import json
import pprint
import os
import re

import requests


def name(filename):
    return os.path.splitext(os.path.split(filename)[-1])[0]


def names(files):
    return [name(f) for f in files]


def get_json():
    """
    Generate the JSON from the Python files.
    """
    py_files = glob.glob('mpconstants/*.py')
    for filename in py_files:
        if filename == 'mozilla_languages':
            raise ValueError('The file mozilla_languages is reserved.')

        filename = name(filename)
        module = 'mpconstants.' + filename
        mod = importlib.import_module(module)

        export = {}
        for k, v in mod.__dict__.items():
            if k.startswith('__') and k.endswith('__'):
                continue
            export[k] = v

        if not export:
            continue

        output = os.path.join('json', filename + '.json')
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
    pretty = pprint.pformat(data.json())
    open('json/mozilla_languages.json', 'w').write(pretty)
    open('mpconstants/mozilla_languages.py', 'w').write(
        u'LANGUAGES = ' + pretty)


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
        pretty = pprint.pformat(data.json())
        open('json/regions/{0}'.format(link), 'w').write(pretty)
        (open('mpconstants/regions/{0}'
              .format(link.replace('.json', '.py').replace('-', '_')), 'w')
              .write(u'REGIONS = ' + pretty))


if __name__ == '__main__':
    get_json()
    get_regions()
    get_languages()
