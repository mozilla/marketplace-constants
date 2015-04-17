from collections import Counter
from unittest import TestCase

from mpconstants.carriers import CARRIER_SLUGS, CARRIER_DETAILS
from mpconstants.countries import COUNTRIES, COUNTRY_DETAILS
from mpconstants.payments import CURRENCIES


class TestCountries(TestCase):

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

    def test_unique_mcs(self):
        # So far, our MCCs have always been unique (and so it's helpful to have
        # this test to detect copy-pasting errors) but it might not be the
        # case in the future. Delete this test if you find out it's actually
        # wrong.
        ids = [c['mcc'] for c in COUNTRY_DETAILS.values()]
        most = Counter(ids).most_common(1)[0]
        assert most[1] == 1, 'Id: %s occurred %s times' % (most[0], most[1])

    def test_valid_currency(self):
        for country in COUNTRY_DETAILS.values():
            assert country['default_currency'] in CURRENCIES, (
                'Country %s has an unkown default currency: %s' %
                (country['name'], country['default_currency']))


class TestCarriers(TestCase):
    def test_valid(self):
        carrier_details = set([c['slug'] for c in CARRIER_DETAILS.values()])
        diff = carrier_details.difference(set(CARRIER_SLUGS))
        assert not diff, 'Extra carriers: %s' % diff

    def test_unique_id(self):
        ids = [c['id'] for c in CARRIER_DETAILS.values()]
        most = Counter(ids).most_common(1)[0]
        assert most[1] == 1, 'Id: %s occurred %s times' % (most[0], most[1])

    def test_unique_slugs(self):
        ids = [c['slug'] for c in CARRIER_DETAILS.values()]
        most = Counter(ids).most_common(1)[0]
        assert most[1] == 1, 'Id: %s occurred %s times' % (most[0], most[1])
