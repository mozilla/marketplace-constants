from collections import Counter
import unittest

from mpconstants.countries import COUNTRIES, COUNTRY_DETAILS


class TestCountries(unittest.TestCase):

    def test_valid(self):
        diff = set(COUNTRY_DETAILS.keys()).difference(set(COUNTRIES))
        assert not diff, 'Extra countries: %s' % diff

    def test_unique_id(self):
        ids = [c['id'] for c in COUNTRY_DETAILS.values()]
        most = Counter(ids).most_common(1)[0]
        assert most[1] == 1, 'Id: %s occurred %s times' % (most[0], most[1])

    def test_unique_slugs(self):
        ids = [c['slug'] for c in COUNTRY_DETAILS.values()]
        most = Counter(ids).most_common(1)[0]
        assert most[1] == 1, 'Id: %s occurred %s times' % (most[0], most[1])
