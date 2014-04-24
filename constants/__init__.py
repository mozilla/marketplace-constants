import glob
import json
import os


class LazyJSON(object):

    def __init__(self, filename):
        self._filename = filename
        self._json = None

    def __getattr__(self, attr):
        if not self._json:
            self._json = json.load(open(self._filename, 'r'))
        return self._json[attr]


for filename in glob.glob('data/*.json'):
    _name, _json = os.path.splitext(filename)
    _name = _name.split('/')[1]
    if not _json:
        continue
    assert _name not in locals()
    locals()[_name] = LazyJSON(filename)
