import glob
import importlib
import json
import os

py_files = glob.glob('constants/*.py')
js_files = glob.glob('js/*.json')


def name(filename):
    return os.path.splitext(os.path.split(filename)[-1])[0]


def names(files):
    return [name(f) for f in files]


for filename in py_files:
    filename = name(filename)
    module = 'constants.' + filename
    mod = importlib.import_module(module)

    export = {}
    for k, v in mod.__dict__.items():
        if k.startswith('__') and k.endswith('__'):
            continue
        export[k] = v

    if not export:
        continue

    output = os.path.join('js', filename + '.json')
    change = 'Updating' if os.path.exists(output) else 'Creating'
    print '{0} file: {1}'.format(change, output)
    json.dump(export, open(output, 'w'), indent=2)


diff = set(names(js_files)).difference(set(names(py_files)))

for filename in diff:
    # Clean up any missing files.
    print 'Deleting file: {0}'.format(filename)
    os.remove(os.path.join('js', filename + '.json'))
