import glob
import importlib
import json
import pprint
import os

import requests


def name(filename):
    return os.path.splitext(os.path.split(filename)[-1])[0]


def names(files):
    return [name(f) for f in files]


def get_json():
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
    remote_lang = ('http://svn.mozilla.org'
                   '/libs/product-details/json/languages.json')
    data = requests.get(remote_lang)
    pretty = pprint.pformat(data.json())
    open('json/mozilla_languages.json', 'w').write(pretty)
    open('mpconstants/mozilla_languages.py', 'w').write(
        u'LANGUAGES = ' + pretty)


def cleanup():
    py_files = glob.glob('mpconstants/*.py')
    json_files = glob.glob('json/*.json')
    diff = set(names(json_files)).difference(set(names(py_files)))
    for filename in diff:
        # Clean up any missing files.
        full = os.path.join('json', filename)
        os.remove(full)
        os.system('git remove {0}'.format(full))

    for filename in json_files:
        os.system('git add {0}'.format(filename))

    for filename in py_files:
        os.system('git add {0}'.format(filename))


if __name__ == '__main__':
    get_json()
    get_languages()
    cleanup()
