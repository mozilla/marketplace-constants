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
import shutil
import sys

import mobile_codes
import requests
import mobile_codes


parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set up partials to easily get the path of a JS/PY file.
JS_PATH = 'dist/js'
CSS_PATH = 'dist/css'
IMG_PATH = 'dist/img'
PY_PATH = 'mpconstants'
LIB_PATH = 'lib'
js_path = partial(os.path.join, parent, JS_PATH)
css_path = partial(os.path.join, parent, CSS_PATH)
img_path = partial(os.path.join, parent, IMG_PATH)
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
    Generate JS modules from the Python files. Without any extra processing.
    """
    js_module_template = open(lib_path('templates/umd.js'), 'r').read()
    py_files = glob.glob(py_path('*.py'))

    for filename in py_files:
        filename = name(filename)
        if filename in ['__init__', 'mozilla_languages']:
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


def build_regions_js():
    """
    Generate a supported regions modules for Marketplace frontend projects.
    Maps from region slug to gettexted region names.
    ex: {'fr': gettext('France'),...}
    """
    js_module_template = open(lib_path('templates/regions.js'), 'r').read()
    countries = name(glob.glob(py_path('countries.py'))[0])
    countries = importlib.import_module(countries)

    # REGION_CHOICES_SLUG: Region slug to gettext mapping.
    data = {
        'REGION_CHOICES_SLUG': {
            'restofworld': "gettext('Rest of World')"
        },
        'MOBILE_CODES': {}
    }
    for k, country in countries.COUNTRY_DETAILS.items():
        data['REGION_CHOICES_SLUG'][country['slug'].lower()] = (
            "gettext('%s')" % country['name'])

    # MOBILE_CODES: Mobile code to region slug mapping.
    for alpha3, country in countries.COUNTRY_DETAILS.items():
        try:
            mccs = mobile_codes.alpha3(alpha3).mcc
        except KeyError:
            mccs = mobile_codes.name(country['name'].lower()).mcc
        if not isinstance(mccs, list):
            mccs = [mccs]
        for mcc in mccs:
            data['MOBILE_CODES'][mcc] = country['slug']

    # Serialize.
    data = json.dumps(data)

    # Unquote the gettexts.
    data = (data.replace('"gettext', 'gettext')
                .replace(')",', '),')
                .replace(')"}}', ')}}'))

    # Write the data.
    output = js_path('regions.js')
    change = 'Updating' if os.path.exists(output) else 'Creating'
    print '{0} file: {1}'.format(change, output)
    open(output, 'w').write(js_module_template % data)


def build_regions_css():
    """
    Generate a regions CSS modules that creates rules to show region background
    images.
    ex: .region-fr { background-image: url('../img/icons/regions/fr.png');}
    """
    css_template = open(lib_path('templates/regions.styl'), 'r').read()
    countries = name(glob.glob(py_path('countries.py'))[0])
    countries = importlib.import_module(countries)

    # Create list of region slugs (e.g., "ar br de fr").
    regions = ''
    for k, country in countries.COUNTRY_DETAILS.items():
        region = country['slug'].lower()
        if region == 'in':
            # Escape Stylus in keyword.
            region = '%r' % region
        regions += ' ' + region
    regions += ' restofworld;'

    # Write the data.
    output = css_path('regions.styl')
    change = 'Updating' if os.path.exists(output) else 'Creating'
    print '{0} file: {1}'.format(change, output)
    open(output, 'w').write(css_template % regions)


def get_region_imgs():
    """
    Set the country flag images in dist/img/regions. Only copy over images for
    supported regions. Delete any images that aren't supported. Supported
    regions are defined in countries.py.COUNTRY_DETAILS.
    """
    try:
        # Delete the directory so we don't have imgs we don't need.
        os.rmdir(img_path('regions'))
        os.mkdir(img_path('regions'))
    except OSError:
        pass

    countries = name(glob.glob(py_path('countries.py'))[0])
    countries = importlib.import_module(countries)
    regions = [country[1]['slug'] for country in
               countries.COUNTRY_DETAILS.items()]

    print 'Copying region flag images'
    for region in regions + ['restofworld']:
        shutil.copy('mpconstants/img/regions/' + region + '.png',
                    'dist/img/regions/')


if __name__ == '__main__':
    get_js_modules()
    get_regions()
    get_languages()
    build_regions_js()
    build_regions_css()
    get_region_imgs()
