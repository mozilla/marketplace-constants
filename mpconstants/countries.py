# -*- coding: utf8 -*-
# List of valid country codes: http://en.wikipedia.org/wiki/ISO_3166-1_alpha-3
COUNTRIES = [
    'ABW', 'AFG', 'AGO', 'AIA', 'ALA', 'ALB', 'AND', 'ARE', 'ARG', 'ARM',
    'ASM', 'ATA', 'ATF', 'ATG', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN',
    'BES', 'BFA', 'BGD', 'BGR', 'BHR', 'BHS', 'BIH', 'BLM', 'BLR', 'BLZ',
    'BMU', 'BOL', 'BRA', 'BRB', 'BRN', 'BTN', 'BVT', 'BWA', 'CAF', 'CAN',
    'CCK', 'CHE', 'CHL', 'CHN', 'CIV', 'CMR', 'COD', 'COG', 'COK', 'COL',
    'COM', 'CPV', 'CRI', 'CUB', 'CUW', 'CXR', 'CYM', 'CYP', 'CZE', 'DEU',
    'DJI', 'DMA', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 'ESH', 'ESP',
    'EST', 'ETH', 'FIN', 'FJI', 'FLK', 'FRA', 'FRO', 'FSM', 'GAB', 'GBR',
    'GEO', 'GGY', 'GHA', 'GIB', 'GIN', 'GLP', 'GMB', 'GNB', 'GNQ', 'GRC',
    'GRD', 'GRL', 'GTM', 'GUF', 'GUM', 'GUY', 'HKG', 'HMD', 'HND', 'HRV',
    'HTI', 'HUN', 'IDN', 'IMN', 'IND', 'IOT', 'IRL', 'IRQ', 'ISL', 'ISR',
    'ITA', 'JAM', 'JEY', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KIR',
    'KNA', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LIE', 'LKA',
    'LSO', 'LTU', 'LUX', 'LVA', 'MAC', 'MAF', 'MAR', 'MCO', 'MDA', 'MDG',
    'MDV', 'MEX', 'MHL', 'MKD', 'MLI', 'MLT', 'MMR', 'MNE', 'MNG', 'MNP',
    'MOZ', 'MRT', 'MSR', 'MTQ', 'MUS', 'MWI', 'MYS', 'MYT', 'NAM', 'NCL',
    'NER', 'NFK', 'NGA', 'NIC', 'NIU', 'NLD', 'NOR', 'NPL', 'NRU', 'NZL',
    'OMN', 'PAK', 'PAN', 'PCN', 'PER', 'PHL', 'PLW', 'PNG', 'POL', 'PRI',
    'PRT', 'PRY', 'PSE', 'PYF', 'QAT', 'REU', 'ROU', 'RUS', 'RWA', 'SAU',
    'SDN', 'SEN', 'SGP', 'SGS', 'SHN', 'SJM', 'SLB', 'SLE', 'SLV', 'SMR',
    'SOM', 'SPM', 'SRB', 'SSD', 'STP', 'SUR', 'SVK', 'SVN', 'SWE', 'SWZ',
    'SXM', 'SYC', 'SYR', 'TCA', 'TCD', 'TGO', 'THA', 'TJK', 'TKL', 'TKM',
    'TLS', 'TON', 'TTO', 'TUN', 'TUR', 'TUV', 'TWN', 'TZA', 'UGA', 'UKR',
    'UMI', 'URY', 'USA', 'UZB', 'VAT', 'VCT', 'VEN', 'VGB', 'VIR', 'VNM',
    'VUT', 'WLF', 'WSM', 'YEM', 'ZAF', 'ZMB', 'ZWE'
]

COUNTRY_DETAILS = {
    'ABW': {
        'adolescent': True,
        'id': 69,
        'name': u'Aruba',
        'ratingsbody': None,
        'slug': 'aw',
        'special': False,
        'weight': 0
    },
    'AFG': {
        'adolescent': True,
        'id': 58,
        'name': u'Afghanistan',
        'ratingsbody': None,
        'slug': 'af',
        'special': False,
        'weight': 0
    },
    'AGO': {
        'adolescent': True,
        'id': 64,
        'name': u'Angola',
        'ratingsbody': None,
        'slug': 'ao',
        'special': False,
        'weight': 0
    },
    'AIA': {
        'adolescent': True,
        'id': 65,
        'name': u'Anguilla',
        'ratingsbody': None,
        'slug': 'ai',
        'special': False,
        'weight': 0
    },
    'ALA': {
        'adolescent': True,
        'id': 59,
        'name': u'\xc5land Islands',
        'ratingsbody': None,
        'slug': 'ax',
        'special': False,
        'weight': 0
    },
    'ALB': {
        'adolescent': True,
        'id': 60,
        'name': u'Albania',
        'ratingsbody': None,
        'slug': 'al',
        'special': False,
        'weight': 0
    },
    'AND': {
        'adolescent': True,
        'id': 63,
        'name': u'Andorra',
        'ratingsbody': None,
        'slug': 'ad',
        'special': False,
        'weight': 0
    },
    'ARE': {
        'adolescent': True,
        'id': 241,
        'name': u'United Arab Emirates',
        'ratingsbody': None,
        'slug': 'ae',
        'special': False,
        'weight': 0
    },
    'ARG': {
        'adolescent': True,
        'id': 20,
        'mcc': 722,
        'name': u'Argentina',
        'ratingsbody': 'ESRB',
        'slug': 'ar',
        'special': False,
        'weight': 0
    },
    'ARM': {
        'adolescent': True,
        'id': 68,
        'name': u'Armenia',
        'ratingsbody': None,
        'slug': 'am',
        'special': False,
        'weight': 0
    },
    'ASM': {
        'adolescent': True,
        'id': 62,
        'name': u'American Samoa',
        'ratingsbody': None,
        'slug': 'as',
        'special': False,
        'weight': 0
    },
    'ATA': {
        'adolescent': True,
        'id': 66,
        'name': u'Antarctica',
        'ratingsbody': None,
        'slug': 'aq',
        'special': False,
        'weight': 0
    },
    'ATF': {
        'adolescent': True,
        'id': 120,
        'name': u'French Southern Territories',
        'ratingsbody': None,
        'slug': 'tf',
        'special': False,
        'weight': 0
    },
    'ATG': {
        'adolescent': True,
        'id': 67,
        'name': u'Antigua and Barbuda',
        'ratingsbody': None,
        'slug': 'ag',
        'special': False,
        'weight': 0
    },
    'AUS': {
        'adolescent': True,
        'id': 70,
        'name': u'Australia',
        'ratingsbody': None,
        'slug': 'au',
        'special': False,
        'weight': 0
    },
    'AUT': {
        'adolescent': True,
        'id': 71,
        'name': u'Austria',
        'ratingsbody': None,
        'slug': 'at',
        'special': False,
        'weight': 0
    },
    'AZE': {
        'adolescent': True,
        'id': 72,
        'name': u'Azerbaijan',
        'ratingsbody': None,
        'slug': 'az',
        'special': False,
        'weight': 0
    },
    'BDI': {
        'adolescent': True,
        'id': 90,
        'name': u'Burundi',
        'ratingsbody': None,
        'slug': 'bi',
        'special': False,
        'weight': 0
    },
    'BEL': {
        'adolescent': True,
        'id': 77,
        'name': u'Belgium',
        'ratingsbody': None,
        'slug': 'be',
        'special': False,
        'weight': 0
    },
    'BEN': {
        'adolescent': True,
        'id': 79,
        'name': u'Benin',
        'ratingsbody': None,
        'slug': 'bj',
        'special': False,
        'weight': 0
    },
    'BES': {
        'adolescent': True,
        'id': 252,
        'name': u'Bonaire, Sint Eustatius and Saba',
        'ratingsbody': None,
        'slug': 'bq',
        'special': False,
        'weight': 0
    },
    'BFA': {
        'adolescent': True,
        'id': 89,
        'name': u'Burkina Faso',
        'ratingsbody': None,
        'slug': 'bf',
        'special': False,
        'weight': 0
    },
    'BGD': {
        'adolescent': True,
        'id': 31,
        'mcc': 470,
        'name': u'Bangladesh',
        'ratingsbody': None,
        'slug': 'bd',
        'special': False,
        'weight': 0
    },
    'BGR': {
        'adolescent': True,
        'id': 88,
        'name': u'Bulgaria',
        'ratingsbody': None,
        'slug': 'bg',
        'special': False,
        'weight': 0
    },
    'BHR': {
        'adolescent': True,
        'id': 74,
        'name': u'Bahrain',
        'ratingsbody': None,
        'slug': 'bh',
        'special': False,
        'weight': 0
    },
    'BHS': {
        'adolescent': True,
        'id': 73,
        'name': u'Bahamas',
        'ratingsbody': None,
        'slug': 'bs',
        'special': False,
        'weight': 0
    },
    'BIH': {
        'adolescent': True,
        'id': 84,
        'name': u'Bosnia and Herzegovina',
        'ratingsbody': None,
        'slug': 'ba',
        'special': False,
        'weight': 0
    },
    'BLM': {
        'adolescent': True,
        'id': 253,
        'name': u'Saint Barthélemy',
        'ratingsbody': None,
        'slug': 'bl',
        'special': False,
        'weight': 0
    },
    'BLR': {
        'adolescent': True,
        'id': 76,
        'name': u'Belarus',
        'ratingsbody': None,
        'slug': 'by',
        'special': False,
        'weight': 0
    },
    'BLZ': {
        'adolescent': True,
        'id': 78,
        'name': u'Belize',
        'ratingsbody': None,
        'slug': 'bz',
        'special': False,
        'weight': 0
    },
    'BMU': {
        'adolescent': True,
        'id': 80,
        'name': u'Bermuda',
        'ratingsbody': None,
        'slug': 'bm',
        'special': False,
        'weight': 0
    },
    'BOL': {
        'adolescent': True,
        'id': 82,
        'name': u'Bolivia, Plurinational State of',
        'ratingsbody': None,
        'slug': 'bo',
        'special': False,
        'weight': 0
    },
    'BRA': {
        'adolescent': False,
        'id': 7,
        'mcc': 724,
        'name': u'Brazil',
        'ratingsbody': 'CLASSIND',
        'slug': 'br',
        'special': False,
        'weight': 0
    },
    'BRB': {
        'adolescent': True,
        'id': 75,
        'name': u'Barbados',
        'ratingsbody': None,
        'slug': 'bb',
        'special': False,
        'weight': 0
    },
    'BRN': {
        'adolescent': True,
        'id': 87,
        'name': u'Brunei Darussalam',
        'ratingsbody': None,
        'slug': 'bn',
        'special': False,
        'weight': 0
    },
    'BTN': {
        'adolescent': True,
        'id': 81,
        'name': u'Bhutan',
        'ratingsbody': None,
        'slug': 'bt',
        'special': False,
        'weight': 0
    },
    'BVT': {
        'adolescent': True,
        'id': 85,
        'name': u'Bouvet Island',
        'ratingsbody': None,
        'slug': 'bv',
        'special': False,
        'weight': 0
    },
    'BWA': {
        'adolescent': True,
        'id': 45,
        'mcc': 652,
        'name': u'Botswana',
        'slug': 'bw',
        'special': False,
        'weight': 0
    },
    'CAF': {
        'adolescent': True,
        'id': 54,
        'mcc': 623,
        'name': u'Central African Republic',
        'slug': 'cf',
        'special': False,
        'weight': 0
    },
    'CAN': {
        'adolescent': True,
        'id': 92,
        'name': u'Canada',
        'ratingsbody': None,
        'slug': 'ca',
        'special': False,
        'weight': 0
    },
    'CCK': {
        'adolescent': True,
        'id': 97,
        'name': u'Cocos (Keeling) Islands',
        'ratingsbody': None,
        'slug': 'cc',
        'special': False,
        'weight': 0
    },
    'CHE': {
        'adolescent': True,
        'id': 226,
        'name': u'Switzerland',
        'ratingsbody': None,
        'slug': 'ch',
        'special': False,
        'weight': 0
    },
    'CHL': {
        'adolescent': True,
        'id': 23,
        'mcc': 730,
        'name': u'Chile',
        'ratingsbody': 'ESRB',
        'slug': 'cl',
        'special': False,
        'weight': 0
    },
    'CHN': {
        'adolescent': True,
        'id': 21,
        'mcc': 460,
        'name': u'China',
        'ratingsbody': None,
        'slug': 'cn',
        'special': True,
        'weight': 0
    },
    'CIV': {
        'adolescent': True,
        'id': 40,
        'mcc': 612,
        'name': u"Côte d'Ivoire",
        'slug': 'ci',
        'special': False,
        'weight': 0
    },
    'CMR': {
        'adolescent': True,
        'id': 42,
        'mcc': 624,
        'name': u'Cameroon',
        'slug': 'cm',
        'special': False,
        'weight': 0
    },
    'COD': {
        'adolescent': True,
        'id': 100,
        'name': u'Congo, Democratic Republic of the',
        'ratingsbody': None,
        'slug': 'cd',
        'special': False,
        'weight': 0
    },
    'COG': {
        'adolescent': True,
        'id': 99,
        'name': u'Congo',
        'ratingsbody': None,
        'slug': 'cg',
        'special': False,
        'weight': 0
    },
    'COK': {
        'adolescent': True,
        'id': 101,
        'name': u'Cook Islands',
        'ratingsbody': None,
        'slug': 'ck',
        'special': False,
        'weight': 0
    },
    'COL': {
        'adolescent': False,
        'id': 9,
        'mcc': 732,
        'name': u'Colombia',
        'ratingsbody': 'ESRB',
        'slug': 'co',
        'special': False,
        'weight': 0
    },
    'COM': {
        'adolescent': True,
        'id': 98,
        'name': u'Comoros',
        'ratingsbody': None,
        'slug': 'km',
        'special': False,
        'weight': 0
    },
    'CPV': {
        'adolescent': True,
        'id': 93,
        'name': u'Cabo Verde',
        'ratingsbody': None,
        'slug': 'cv',
        'special': False,
        'weight': 0
    },
    'CRI': {
        'adolescent': True,
        'id': 27,
        'mcc': 712,
        'name': u'Costa Rica',
        'ratingsbody': 'ESRB',
        'slug': 'cr',
        'special': False,
        'weight': 0
    },
    'CUB': {
        'adolescent': True,
        'id': 103,
        'name': u'Cuba',
        'ratingsbody': None,
        'slug': 'cu',
        'special': False,
        'weight': 0
    },
    'CUW': {
        'adolescent': True,
        'id': 254,
        'name': u'Cura\xe7ao',
        'ratingsbody': None,
        'slug': 'cw',
        'special': False,
        'weight': 0
    },
    'CXR': {
        'adolescent': True,
        'id': 96,
        'name': u'Christmas Island',
        'ratingsbody': None,
        'slug': 'cx',
        'special': False,
        'weight': 0
    },
    'CYM': {
        'adolescent': True,
        'id': 94,
        'name': u'Cayman Islands',
        'ratingsbody': None,
        'slug': 'ky',
        'special': False,
        'weight': 0
    },
    'CYP': {
        'adolescent': True,
        'id': 105,
        'name': u'Cyprus',
        'ratingsbody': None,
        'slug': 'cy',
        'special': False,
        'weight': 0
    },
    'CZE': {
        'adolescent': True,
        'id': 34,
        'mcc': 230,
        'name': u'Czech Republic',
        'slug': 'cz',
        'special': False,
        'weight': 0
    },
    'DEU': {
        'adolescent': True,
        'id': 14,
        'mcc': 262,
        'name': u'Germany',
        'ratingsbody': 'USK',
        'slug': 'de',
        'special': False,
        'weight': 0
    },
    'DJI': {
        'adolescent': True,
        'id': 107,
        'name': u'Djibouti',
        'ratingsbody': None,
        'slug': 'dj',
        'special': False,
        'weight': 0
    },
    'DMA': {
        'adolescent': True,
        'id': 108,
        'name': u'Dominica',
        'ratingsbody': None,
        'slug': 'dm',
        'special': False,
        'weight': 0
    },
    'DNK': {
        'adolescent': True,
        'id': 106,
        'name': u'Denmark',
        'ratingsbody': None,
        'slug': 'dk',
        'special': False,
        'weight': 0
    },
    'DOM': {
        'adolescent': True,
        'id': 109,
        'name': u'Dominican Republic',
        'ratingsbody': None,
        'slug': 'do',
        'special': False,
        'weight': 0
    },
    'DZA': {
        'adolescent': True,
        'id': 61,
        'name': u'Algeria',
        'ratingsbody': None,
        'slug': 'dz',
        'special': False,
        'weight': 0
    },
    'ECU': {
        'adolescent': True,
        'id': 26,
        'mcc': 740,
        'name': u'Ecuador',
        'ratingsbody': 'ESRB',
        'slug': 'ec',
        'special': False,
        'weight': 0
    },
    'EGY': {
        'adolescent': True,
        'id': 43,
        'mcc': 602,
        'name': u'Egypt',
        'slug': 'eg',
        'special': False,
        'weight': 0
    },
    'ERI': {
        'adolescent': True,
        'id': 111,
        'name': u'Eritrea',
        'ratingsbody': None,
        'slug': 'er',
        'special': False,
        'weight': 0
    },
    'ESH': {
        'adolescent': True,
        'id': 248,
        'name': u'Western Sahara',
        'ratingsbody': None,
        'slug': 'eh',
        'special': False,
        'weight': 0
    },
    'ESP': {
        'adolescent': True,
        'id': 8,
        'mcc': 214,
        'name': u'Spain',
        'ratingsbody': 'PEGI',
        'slug': 'es',
        'special': False,
        'weight': 0
    },
    'EST': {
        'adolescent': True,
        'id': 112,
        'name': u'Estonia',
        'ratingsbody': None,
        'slug': 'ee',
        'special': False,
        'weight': 0
    },
    'ETH': {
        'adolescent': True,
        'id': 113,
        'name': u'Ethiopia',
        'ratingsbody': None,
        'slug': 'et',
        'special': False,
        'weight': 0
    },
    'FIN': {
        'adolescent': True,
        'id': 117,
        'name': u'Finland',
        'ratingsbody': None,
        'slug': 'fi',
        'special': False,
        'weight': 0
    },
    'FJI': {
        'adolescent': True,
        'id': 116,
        'name': u'Fiji',
        'ratingsbody': None,
        'slug': 'fj',
        'special': False,
        'weight': 0
    },
    'FLK': {
        'adolescent': True,
        'id': 114,
        'name': u'Falkland Islands (Malvinas)',
        'ratingsbody': None,
        'slug': 'fk',
        'special': False,
        'weight': 0
    },
    'FRA': {
        'adolescent': True,
        'id': 30,
        'mcc': 208,
        'name': u'France',
        'ratingsbody': 'PEGI',
        'slug': 'fr',
        'special': False,
        'weight': 0
    },
    'FRO': {
        'adolescent': True,
        'id': 115,
        'name': u'Faroe Islands',
        'ratingsbody': None,
        'slug': 'fo',
        'special': False,
        'weight': 0
    },
    'FSM': {
        'adolescent': True,
        'id': 168,
        'name': u'Micronesia, Federated States of',
        'ratingsbody': None,
        'slug': 'fm',
        'special': False,
        'weight': 0
    },
    'GAB': {
        'adolescent': True,
        'id': 121,
        'name': u'Gabon',
        'ratingsbody': None,
        'slug': 'ga',
        'special': False,
        'weight': 0
    },
    'GBR': {
        'adolescent': True,
        'id': 4,
        'mcc': 235,
        'name': u'United Kingdom',
        'ratingsbody': 'PEGI',
        'slug': 'uk',
        'special': False,
        'weight': 0
    },
    'GEO': {
        'adolescent': True,
        'id': 123,
        'name': u'Georgia',
        'ratingsbody': None,
        'slug': 'ge',
        'special': False,
        'weight': 0
    },
    'GGY': {
        'adolescent': True,
        'id': 130,
        'name': u'Guernsey',
        'ratingsbody': None,
        'slug': 'gg',
        'special': False,
        'weight': 0
    },
    'GHA': {
        'adolescent': True,
        'id': 124,
        'name': u'Ghana',
        'ratingsbody': None,
        'slug': 'gh',
        'special': False,
        'weight': 0
    },
    'GIB': {
        'adolescent': True,
        'id': 125,
        'name': u'Gibraltar',
        'ratingsbody': None,
        'slug': 'gi',
        'special': False,
        'weight': 0
    },
    'GIN': {
        'adolescent': True,
        'id': 55,
        'mcc': 611,
        'name': u'Guinea-Conakry',
        'slug': 'gn',
        'special': False,
        'weight': 0
    },
    'GLP': {
        'adolescent': True,
        'id': 128,
        'name': u'Guadeloupe',
        'ratingsbody': None,
        'slug': 'gp',
        'special': False,
        'weight': 0
    },
    'GMB': {
        'adolescent': True,
        'id': 122,
        'name': u'Gambia',
        'ratingsbody': None,
        'slug': 'gm',
        'special': False,
        'weight': 0
    },
    'GNB': {
        'adolescent': True,
        'id': 46,
        'mcc': 632,
        'name': u'Guinea-Bissau',
        'slug': 'gw',
        'special': False,
        'weight': 0
    },
    'GNQ': {
        'adolescent': True,
        'id': 110,
        'name': u'Equatorial Guinea',
        'ratingsbody': None,
        'slug': 'gq',
        'special': False,
        'weight': 0
    },
    'GRC': {
        'adolescent': True,
        'id': 17,
        'mcc': 202,
        'name': u'Greece',
        'ratingsbody': 'PEGI',
        'slug': 'gr',
        'special': False,
        'weight': 0
    },
    'GRD': {
        'adolescent': True,
        'id': 127,
        'name': u'Grenada',
        'ratingsbody': None,
        'slug': 'gd',
        'special': False,
        'weight': 0
    },
    'GRL': {
        'adolescent': True,
        'id': 126,
        'name': u'Greenland',
        'ratingsbody': None,
        'slug': 'gl',
        'special': False,
        'weight': 0
    },
    'GTM': {
        'adolescent': True,
        'id': 25,
        'mcc': 704,
        'name': u'Guatemala',
        'ratingsbody': 'ESRB',
        'slug': 'gt',
        'special': False,
        'weight': 0
    },
    'GUF': {
        'adolescent': True,
        'id': 118,
        'name': u'French Guiana',
        'ratingsbody': None,
        'slug': 'gf',
        'special': False,
        'weight': 0
    },
    'GUM': {
        'adolescent': True,
        'id': 129,
        'name': u'Guam',
        'ratingsbody': None,
        'slug': 'gu',
        'special': False,
        'weight': 0
    },
    'GUY': {
        'adolescent': True,
        'id': 131,
        'name': u'Guyana',
        'ratingsbody': None,
        'slug': 'gy',
        'special': False,
        'weight': 0
    },
    'HKG': {
        'adolescent': True,
        'id': 136,
        'name': u'Hong Kong',
        'ratingsbody': None,
        'slug': 'hk',
        'special': False,
        'weight': 0
    },
    'HMD': {
        'adolescent': True,
        'id': 133,
        'name': u'Heard Island and McDonald Islands',
        'ratingsbody': None,
        'slug': 'hm',
        'special': False,
        'weight': 0
    },
    'HND': {
        'adolescent': True,
        'id': 135,
        'name': u'Honduras',
        'ratingsbody': None,
        'slug': 'hn',
        'special': False,
        'weight': 0
    },
    'HRV': {
        'adolescent': True,
        'id': 102,
        'name': u'Croatia',
        'ratingsbody': None,
        'slug': 'hr',
        'special': False,
        'weight': 0
    },
    'HTI': {
        'adolescent': True,
        'id': 132,
        'name': u'Haiti',
        'ratingsbody': None,
        'slug': 'ht',
        'special': False,
        'weight': 0
    },
    'HUN': {
        'adolescent': True,
        'id': 13,
        'mcc': 216,
        'name': u'Hungary',
        'ratingsbody': 'PEGI',
        'slug': 'hu',
        'special': False,
        'weight': 0
    },
    'IDN': {
        'adolescent': True,
        'id': 138,
        'name': u'Indonesia',
        'ratingsbody': None,
        'slug': 'id',
        'special': False,
        'weight': 0
    },
    'IMN': {
        'adolescent': True,
        'id': 141,
        'name': u'Isle of Man',
        'ratingsbody': None,
        'slug': 'im',
        'special': False,
        'weight': 0
    },
    'IND': {
        'adolescent': True,
        'id': 32,
        'low_memory': True,
        'mcc': 405,
        'name': u'India',
        'ratingsbody': None,
        'slug': 'in',
        'weight': 0
    },
    'IOT': {
        'adolescent': True,
        'id': 86,
        'name': u'British Indian Ocean Territory',
        'ratingsbody': None,
        'slug': 'io',
        'special': False,
        'weight': 0
    },
    'IRL': {
        'adolescent': True,
        'id': 140,
        'name': u'Ireland',
        'ratingsbody': None,
        'slug': 'ie',
        'special': False,
        'weight': 0
    },
    'IRQ': {
        'adolescent': True,
        'id': 139,
        'name': u'Iraq',
        'ratingsbody': None,
        'slug': 'iq',
        'special': False,
        'weight': 0
    },
    'ISL': {
        'adolescent': True,
        'id': 137,
        'name': u'Iceland',
        'ratingsbody': None,
        'slug': 'is',
        'special': False,
        'weight': 0
    },
    'ISR': {
        'adolescent': True,
        'id': 142,
        'name': u'Israel',
        'ratingsbody': None,
        'slug': 'il',
        'special': False,
        'weight': 0
    },
    'ITA': {
        'adolescent': True,
        'id': 22,
        'mcc': 222,
        'name': u'Italy',
        'ratingsbody': 'PEGI',
        'slug': 'it',
        'special': False,
        'weight': 0
    },
    'JAM': {
        'adolescent': True,
        'id': 143,
        'name': u'Jamaica',
        'ratingsbody': None,
        'slug': 'jm',
        'special': False,
        'weight': 0
    },
    'JEY': {
        'adolescent': True,
        'id': 144,
        'name': u'Jersey',
        'ratingsbody': None,
        'slug': 'je',
        'special': False,
        'weight': 0
    },
    'JOR': {
        'adolescent': True,
        'id': 51,
        'mcc': 416,
        'name': u'Jordan',
        'slug': 'jo',
        'special': False,
        'weight': 0
    },
    'JPN': {
        'adolescent': True,
        'id': 33,
        'mcc': 440,
        'name': u'Japan',
        'slug': 'jp',
        'special': False,
        'weight': 0
    },
    'KAZ': {
        'adolescent': True,
        'id': 145,
        'name': u'Kazakhstan',
        'ratingsbody': None,
        'slug': 'kz',
        'special': False,
        'weight': 0
    },
    'KEN': {
        'adolescent': True,
        'id': 56,
        'mcc': 639,
        'name': u'Kenya',
        'slug': 'ke',
        'special': False,
        'weight': 0
    },
    'KGZ': {
        'adolescent': True,
        'id': 149,
        'name': u'Kyrgyzstan',
        'ratingsbody': None,
        'slug': 'kg',
        'special': False,
        'weight': 0
    },
    'KHM': {
        'adolescent': True,
        'id': 91,
        'name': u'Cambodia',
        'ratingsbody': None,
        'slug': 'kh',
        'special': False,
        'weight': 0
    },
    'KIR': {
        'adolescent': True,
        'id': 146,
        'name': u'Kiribati',
        'ratingsbody': None,
        'slug': 'ki',
        'special': False,
        'weight': 0
    },
    'KNA': {
        'adolescent': True,
        'id': 201,
        'name': u'Saint Kitts and Nevis',
        'ratingsbody': None,
        'slug': 'kn',
        'special': False,
        'weight': 0
    },
    'KOR': {
        'adolescent': True,
        'id': 147,
        'name': u'Korea, Republic of',
        'ratingsbody': None,
        'slug': 'kr',
        'special': False,
        'weight': 0
    },
    'KWT': {
        'adolescent': True,
        'id': 148,
        'name': u'Kuwait',
        'ratingsbody': None,
        'slug': 'kw',
        'special': False,
        'weight': 0
    },
    'LAO': {
        'adolescent': True,
        'id': 150,
        'name': u"Lao People's Democratic Republic",
        'ratingsbody': None,
        'slug': 'la',
        'special': False,
        'weight': 0
    },
    'LBN': {
        'adolescent': True,
        'id': 152,
        'name': u'Lebanon',
        'ratingsbody': None,
        'slug': 'lb',
        'special': False,
        'weight': 0
    },
    'LBR': {
        'adolescent': True,
        'id': 154,
        'name': u'Liberia',
        'ratingsbody': None,
        'slug': 'lr',
        'special': False,
        'weight': 0
    },
    'LBY': {
        'adolescent': True,
        'id': 155,
        'name': u'Libya',
        'ratingsbody': None,
        'slug': 'ly',
        'special': False,
        'weight': 0
    },
    'LCA': {
        'adolescent': True,
        'id': 202,
        'name': u'Saint Lucia',
        'ratingsbody': None,
        'slug': 'lc',
        'special': False,
        'weight': 0
    },
    'LIE': {
        'adolescent': True,
        'id': 156,
        'name': u'Liechtenstein',
        'ratingsbody': None,
        'slug': 'li',
        'special': False,
        'weight': 0
    },
    'LKA': {
        'adolescent': True,
        'id': 220,
        'name': u'Sri Lanka',
        'ratingsbody': None,
        'slug': 'lk',
        'special': False,
        'weight': 0
    },
    'LSO': {
        'adolescent': True,
        'id': 153,
        'name': u'Lesotho',
        'ratingsbody': None,
        'slug': 'ls',
        'special': False,
        'weight': 0
    },
    'LTU': {
        'adolescent': True,
        'id': 38,
        'mcc': 370,
        'name': u'Lithuania',
        'slug': 'lt',
        'special': False,
        'weight': 0
    },
    'LUX': {
        'adolescent': True,
        'id': 157,
        'name': u'Luxembourg',
        'ratingsbody': None,
        'slug': 'lu',
        'special': False,
        'weight': 0
    },
    'LVA': {
        'adolescent': True,
        'id': 151,
        'name': u'Latvia',
        'ratingsbody': None,
        'slug': 'lv',
        'special': False,
        'weight': 0
    },
    'MAC': {
        'adolescent': True,
        'id': 158,
        'name': u'Macao',
        'ratingsbody': None,
        'slug': 'mo',
        'special': False,
        'weight': 0
    },
    'MAF': {
        'adolescent': True,
        'id': 255,
        'mcc': 340,
        'name': u'Saint Martin (French part)',
        'ratingsbody': None,
        'slug': 'mf',
        'special': False,
        'weight': 0
    },
    'MAR': {
        'adolescent': True,
        'id': 173,
        'name': u'Morocco',
        'ratingsbody': None,
        'slug': 'ma',
        'special': False,
        'weight': 0
    },
    'MCO': {
        'adolescent': True,
        'id': 170,
        'name': u'Monaco',
        'ratingsbody': None,
        'slug': 'mc',
        'special': False,
        'weight': 0
    },
    'MDA': {
        'adolescent': True,
        'id': 169,
        'name': u'Moldova, Republic of',
        'ratingsbody': None,
        'slug': 'md',
        'special': False,
        'weight': 0
    },
    'MDG': {
        'adolescent': True,
        'id': 49,
        'mcc': 646,
        'name': u'Madagascar',
        'slug': 'mg',
        'special': False,
        'weight': 0
    },
    'MDV': {
        'adolescent': True,
        'id': 162,
        'name': u'Maldives',
        'ratingsbody': None,
        'slug': 'mv',
        'special': False,
        'weight': 0
    },
    'MEX': {
        'adolescent': False,
        'id': 12,
        'mcc': 334,
        'name': u'Mexico',
        'ratingsbody': 'ESRB',
        'slug': 'mx',
        'special': False,
        'weight': 0
    },
    'MHL': {
        'adolescent': True,
        'id': 164,
        'name': u'Marshall Islands',
        'ratingsbody': None,
        'slug': 'mh',
        'special': False,
        'weight': 0
    },
    'MKD': {
        'adolescent': True,
        'id': 159,
        'name': u'Macedonia, the former Yugoslav Republic of',
        'ratingsbody': None,
        'slug': 'mk',
        'special': False,
        'weight': 0
    },
    'MLI': {
        'adolescent': True,
        'id': 48,
        'mcc': 610,
        'name': u'Mali',
        'slug': 'ml',
        'special': False,
        'weight': 0
    },
    'MLT': {
        'adolescent': True,
        'id': 163,
        'name': u'Malta',
        'ratingsbody': None,
        'slug': 'mt',
        'special': False,
        'weight': 0
    },
    'MMR': {
        'adolescent': True,
        'id': 53,
        'mcc': 414,
        'name': u'Myanmar',
        'slug': 'mm',
        'special': False,
        'weight': 0
    },
    'MNE': {
        'adolescent': True,
        'id': 15,
        'mcc': 297,
        'name': u'Montenegro',
        'ratingsbody': 'PEGI',
        'slug': 'me',
        'special': False,
        'weight': 0
    },
    'MNG': {
        'adolescent': True,
        'id': 171,
        'name': u'Mongolia',
        'ratingsbody': None,
        'slug': 'mn',
        'special': False,
        'weight': 0
    },
    'MNP': {
        'adolescent': True,
        'id': 184,
        'name': u'Northern Mariana Islands',
        'ratingsbody': None,
        'slug': 'mp',
        'special': False,
        'weight': 0
    },
    'MOZ': {
        'adolescent': True,
        'id': 174,
        'name': u'Mozambique',
        'ratingsbody': None,
        'slug': 'mz',
        'special': False,
        'weight': 0
    },
    'MRT': {
        'adolescent': True,
        'id': 166,
        'name': u'Mauritania',
        'ratingsbody': None,
        'slug': 'mr',
        'special': False,
        'weight': 0
    },
    'MSR': {
        'adolescent': True,
        'id': 172,
        'name': u'Montserrat',
        'ratingsbody': None,
        'slug': 'ms',
        'special': False,
        'weight': 0
    },
    'MTQ': {
        'adolescent': True,
        'id': 165,
        'name': u'Martinique',
        'ratingsbody': None,
        'slug': 'mq',
        'special': False,
        'weight': 0
    },
    'MUS': {
        'adolescent': True,
        'id': 50,
        'mcc': 617,
        'name': u'Mauritius',
        'slug': 'mu',
        'special': False,
        'weight': 0
    },
    'MWI': {
        'adolescent': True,
        'id': 160,
        'name': u'Malawi',
        'ratingsbody': None,
        'slug': 'mw',
        'special': False,
        'weight': 0
    },
    'MYS': {
        'adolescent': True,
        'id': 161,
        'name': u'Malaysia',
        'ratingsbody': None,
        'slug': 'my',
        'special': False,
        'weight': 0
    },
    'MYT': {
        'adolescent': True,
        'id': 167,
        'name': u'Mayotte',
        'ratingsbody': None,
        'slug': 'yt',
        'special': False,
        'weight': 0
    },
    'NAM': {
        'adolescent': True,
        'id': 175,
        'name': u'Namibia',
        'ratingsbody': None,
        'slug': 'na',
        'special': False,
        'weight': 0
    },
    'NCL': {
        'adolescent': True,
        'id': 179,
        'name': u'New Caledonia',
        'ratingsbody': None,
        'slug': 'nc',
        'special': False,
        'weight': 0
    },
    'NER': {
        'adolescent': True,
        'id': 52,
        'mcc': 614,
        'name': u'Niger',
        'slug': 'ne',
        'special': False,
        'weight': 0
    },
    'NFK': {
        'adolescent': True,
        'id': 183,
        'name': u'Norfolk Island',
        'ratingsbody': None,
        'slug': 'nf',
        'special': False,
        'weight': 0
    },
    'NGA': {
        'adolescent': True,
        'id': 181,
        'name': u'Nigeria',
        'ratingsbody': None,
        'slug': 'ng',
        'special': False,
        'weight': 0
    },
    'NIC': {
        'adolescent': True,
        'id': 29,
        'mcc': 710,
        'name': u'Nicaragua',
        'ratingsbody': 'ESRB',
        'slug': 'ni',
        'special': False,
        'weight': 0
    },
    'NIU': {
        'adolescent': True,
        'id': 182,
        'name': u'Niue',
        'ratingsbody': None,
        'slug': 'nu',
        'special': False,
        'weight': 0
    },
    'NLD': {
        'adolescent': True,
        'id': 178,
        'name': u'Netherlands',
        'ratingsbody': None,
        'slug': 'nl',
        'special': False,
        'weight': 0
    },
    'NOR': {
        'adolescent': True,
        'id': 185,
        'name': u'Norway',
        'ratingsbody': None,
        'slug': 'no',
        'special': False,
        'weight': 0
    },
    'NPL': {
        'adolescent': True,
        'id': 177,
        'name': u'Nepal',
        'ratingsbody': None,
        'slug': 'np',
        'special': False,
        'weight': 0
    },
    'NRU': {
        'adolescent': True,
        'id': 176,
        'name': u'Nauru',
        'ratingsbody': None,
        'slug': 'nr',
        'special': False,
        'weight': 0
    },
    'NZL': {
        'adolescent': True,
        'id': 180,
        'name': u'New Zealand',
        'ratingsbody': None,
        'slug': 'nz',
        'special': False,
        'weight': 0
    },
    'OMN': {
        'adolescent': True,
        'id': 186,
        'name': u'Oman',
        'ratingsbody': None,
        'slug': 'om',
        'special': False,
        'weight': 0
    },
    'PAK': {
        'adolescent': True,
        'id': 187,
        'name': u'Pakistan',
        'ratingsbody': None,
        'slug': 'pk',
        'special': False,
        'weight': 0
    },
    'PAN': {
        'adolescent': True,
        'id': 28,
        'mcc': 714,
        'name': u'Panama',
        'ratingsbody': 'ESRB',
        'slug': 'pa',
        'special': False,
        'weight': 0
    },
    'PCN': {
        'adolescent': True,
        'id': 192,
        'name': u'Pitcairn',
        'ratingsbody': None,
        'slug': 'pn',
        'special': False,
        'weight': 0
    },
    'PER': {
        'adolescent': False,
        'id': 18,
        'mcc': 716,
        'name': u'Peru',
        'ratingsbody': 'ESRB',
        'slug': 'pe',
        'special': False,
        'weight': 0
    },
    'PHL': {
        'adolescent': True,
        'id': 35,
        'low_memory': True,
        'mcc': 515,
        'name': u'Philippines',
        'ratingsbody': None,
        'slug': 'ph',
        'weight': 0
    },
    'PLW': {
        'adolescent': True,
        'id': 188,
        'name': u'Palau',
        'ratingsbody': None,
        'slug': 'pw',
        'special': False,
        'weight': 0
    },
    'PNG': {
        'adolescent': True,
        'id': 190,
        'name': u'Papua New Guinea',
        'ratingsbody': None,
        'slug': 'pg',
        'special': False,
        'weight': 0
    },
    'POL': {
        'adolescent': True,
        'id': 11,
        'mcc': 260,
        'name': u'Poland',
        'ratingsbody': 'PEGI',
        'slug': 'pl',
        'special': False,
        'weight': 0
    },
    'PRI': {
        'adolescent': True,
        'id': 194,
        'name': u'Puerto Rico',
        'ratingsbody': None,
        'slug': 'pr',
        'special': False,
        'weight': 0
    },
    'PRT': {
        'adolescent': True,
        'id': 193,
        'name': u'Portugal',
        'ratingsbody': None,
        'slug': 'pt',
        'special': False,
        'weight': 0
    },
    'PRY': {
        'adolescent': True,
        'id': 191,
        'name': u'Paraguay',
        'ratingsbody': None,
        'slug': 'py',
        'special': False,
        'weight': 0
    },
    'PSE': {
        'adolescent': True,
        'id': 189,
        'name': u'Palestine, State of',
        'ratingsbody': None,
        'slug': 'ps',
        'special': False,
        'weight': 0
    },
    'PYF': {
        'adolescent': True,
        'id': 119,
        'name': u'French Polynesia',
        'ratingsbody': None,
        'slug': 'pf',
        'special': False,
        'weight': 0
    },
    'QAT': {
        'adolescent': True,
        'id': 195,
        'name': u'Qatar',
        'ratingsbody': None,
        'slug': 'qa',
        'special': False,
        'weight': 0
    },
    'REU': {
        'adolescent': True,
        'id': 196,
        'name': u'R\xe9union',
        'ratingsbody': None,
        'slug': 're',
        'special': False,
        'weight': 0
    },
    'ROU': {
        'adolescent': True,
        'id': 197,
        'name': u'Romania',
        'ratingsbody': None,
        'slug': 'ro',
        'special': False,
        'weight': 0
    },
    'RUS': {
        'adolescent': True,
        'id': 36,
        'mcc': 250,
        'name': u'Russia',
        'slug': 'ru',
        'special': False,
        'weight': 0
    },
    'RWA': {
        'adolescent': True,
        'id': 198,
        'name': u'Rwanda',
        'ratingsbody': None,
        'slug': 'rw',
        'special': False,
        'weight': 0
    },
    'SAU': {
        'adolescent': True,
        'id': 209,
        'name': u'Saudi Arabia',
        'ratingsbody': None,
        'slug': 'sa',
        'special': False,
        'weight': 0
    },
    'SDN': {
        'adolescent': True,
        'id': 221,
        'name': u'Sudan',
        'ratingsbody': None,
        'slug': 'sd',
        'special': False,
        'weight': 0
    },
    'SEN': {
        'adolescent': True,
        'id': 41,
        'mcc': 608,
        'name': u'Senegal',
        'slug': 'sn',
        'special': False,
        'weight': 0
    },
    'SGP': {
        'adolescent': True,
        'id': 212,
        'name': u'Singapore',
        'ratingsbody': None,
        'slug': 'sg',
        'special': False,
        'weight': 0
    },
    'SGS': {
        'adolescent': True,
        'id': 218,
        'name': u'South Georgia and the South Sandwich Islands',
        'ratingsbody': None,
        'slug': 'gs',
        'special': False,
        'weight': 0
    },
    'SHN': {
        'adolescent': True,
        'id': 200,
        'name': u'Saint Helena, Ascension and Tristan da Cunha',
        'ratingsbody': None,
        'slug': 'sh',
        'special': False,
        'weight': 0
    },
    'SJM': {
        'adolescent': True,
        'id': 223,
        'name': u'Svalbard and Jan Mayen',
        'ratingsbody': None,
        'slug': 'sj',
        'special': False,
        'weight': 0
    },
    'SLB': {
        'adolescent': True,
        'id': 216,
        'name': u'Solomon Islands',
        'ratingsbody': None,
        'slug': 'sb',
        'special': False,
        'weight': 0
    },
    'SLE': {
        'adolescent': True,
        'id': 211,
        'name': u'Sierra Leone',
        'ratingsbody': None,
        'slug': 'sl',
        'special': False,
        'weight': 0
    },
    'SLV': {
        'adolescent': True,
        'id': 24,
        'mcc': 706,
        'name': u'El Salvador',
        'ratingsbody': 'ESRB',
        'slug': 'sv',
        'special': False,
        'weight': 0
    },
    'SMR': {
        'adolescent': True,
        'id': 207,
        'name': u'San Marino',
        'ratingsbody': None,
        'slug': 'sm',
        'special': False,
        'weight': 0
    },
    'SOM': {
        'adolescent': True,
        'id': 217,
        'name': u'Somalia',
        'ratingsbody': None,
        'slug': 'so',
        'special': False,
        'weight': 0
    },
    'SPM': {
        'adolescent': True,
        'id': 204,
        'name': u'Saint Pierre and Miquelon',
        'ratingsbody': None,
        'slug': 'pm',
        'special': False,
        'weight': 0
    },
    'SRB': {
        'adolescent': True,
        'id': 16,
        'mcc': 220,
        'name': u'Serbia',
        'ratingsbody': 'PEGI',
        'slug': 'rs',
        'special': False,
        'weight': 0
    },
    'SSD': {
        'adolescent': True,
        'id': 219,
        'name': u'South Sudan',
        'ratingsbody': None,
        'slug': 'ss',
        'special': False,
        'weight': 0
    },
    'STP': {
        'adolescent': True,
        'id': 208,
        'name': u'Sao Tome and Principe',
        'ratingsbody': None,
        'slug': 'st',
        'special': False,
        'weight': 0
    },
    'SUR': {
        'adolescent': True,
        'id': 222,
        'name': u'Suriname',
        'ratingsbody': None,
        'slug': 'sr',
        'special': False,
        'weight': 0
    },
    'SVK': {
        'adolescent': True,
        'id': 214,
        'name': u'Slovakia',
        'ratingsbody': None,
        'slug': 'sk',
        'special': False,
        'weight': 0
    },
    'SVN': {
        'adolescent': True,
        'id': 215,
        'name': u'Slovenia',
        'ratingsbody': None,
        'slug': 'si',
        'special': False,
        'weight': 0
    },
    'SWE': {
        'adolescent': True,
        'id': 225,
        'name': u'Sweden',
        'ratingsbody': None,
        'slug': 'se',
        'special': False,
        'weight': 0
    },
    'SWZ': {
        'adolescent': True,
        'id': 224,
        'name': u'Swaziland',
        'ratingsbody': None,
        'slug': 'sz',
        'special': False,
        'weight': 0
    },
    'SXM': {
        'adolescent': True,
        'id': 256,
        'name': u'Sint Maarten (Dutch part)',
        'ratingsbody': None,
        'slug': 'sx',
        'special': False,
        'weight': 0
    },
    'SYC': {
        'adolescent': True,
        'id': 210,
        'name': u'Seychelles',
        'ratingsbody': None,
        'slug': 'sc',
        'special': False,
        'weight': 0
    },
    'SYR': {
        'adolescent': True,
        'id': 227,
        'name': u'Syrian Arab Republic',
        'ratingsbody': None,
        'slug': 'sy',
        'special': False,
        'weight': 0
    },
    'TCA': {
        'adolescent': True,
        'id': 237,
        'name': u'Turks and Caicos Islands',
        'ratingsbody': None,
        'slug': 'tc',
        'special': False,
        'weight': 0
    },
    'TCD': {
        'adolescent': True,
        'id': 95,
        'name': u'Chad',
        'ratingsbody': None,
        'slug': 'td',
        'special': False,
        'weight': 0
    },
    'TGO': {
        'adolescent': True,
        'id': 231,
        'name': u'Togo',
        'ratingsbody': None,
        'slug': 'tg',
        'special': False,
        'weight': 0
    },
    'THA': {
        'adolescent': True,
        'id': 229,
        'name': u'Thailand',
        'ratingsbody': None,
        'slug': 'th',
        'special': False,
        'weight': 0
    },
    'TJK': {
        'adolescent': True,
        'id': 228,
        'name': u'Tajikistan',
        'ratingsbody': None,
        'slug': 'tj',
        'special': False,
        'weight': 0
    },
    'TKL': {
        'adolescent': True,
        'id': 232,
        'name': u'Tokelau',
        'ratingsbody': None,
        'slug': 'tk',
        'special': False,
        'weight': 0
    },
    'TKM': {
        'adolescent': True,
        'id': 236,
        'name': u'Turkmenistan',
        'ratingsbody': None,
        'slug': 'tm',
        'special': False,
        'weight': 0
    },
    'TLS': {
        'adolescent': True,
        'id': 230,
        'name': u'Timor-Leste',
        'ratingsbody': None,
        'slug': 'tl',
        'special': False,
        'weight': 0
    },
    'TON': {
        'adolescent': True,
        'id': 233,
        'name': u'Tonga',
        'ratingsbody': None,
        'slug': 'to',
        'special': False,
        'weight': 0
    },
    'TTO': {
        'adolescent': True,
        'id': 234,
        'name': u'Trinidad and Tobago',
        'ratingsbody': None,
        'slug': 'tt',
        'special': False,
        'weight': 0
    },
    'TUN': {
        'adolescent': True,
        'id': 39,
        'mcc': 605,
        'name': u'Tunisia',
        'slug': 'tn',
        'special': False,
        'weight': 0
    },
    'TUR': {
        'adolescent': True,
        'id': 235,
        'name': u'Turkey',
        'ratingsbody': None,
        'slug': 'tr',
        'special': False,
        'weight': 0
    },
    'TUV': {
        'adolescent': True,
        'id': 238,
        'name': u'Tuvalu',
        'ratingsbody': None,
        'slug': 'tv',
        'special': False,
        'weight': 0
    },
    'TWN': {
        'adolescent': True,
        'id': 57,
        'mcc': 466,
        'name': u'Taiwan',
        'slug': 'tw',
        'special': False,
        'weight': 0
    },
    'TZA': {
        'adolescent': True,
        'id': 44,
        'mcc': 640,
        'name': u'Tanzania',
        'slug': 'tz',
        'special': False,
        'weight': 0
    },
    'UGA': {
        'adolescent': True,
        'id': 239,
        'name': u'Uganda',
        'ratingsbody': None,
        'slug': 'ug',
        'special': False,
        'weight': 0
    },
    'UKR': {
        'adolescent': True,
        'id': 240,
        'name': u'Ukraine',
        'ratingsbody': None,
        'slug': 'ua',
        'special': False,
        'weight': 0
    },
    'UMI': {
        'adolescent': True,
        'id': 257,
        'name': u'United States Minor Outlying Islands',
        'ratingsbody': None,
        'slug': 'um',
        'special': False,
        'weight': 0
    },
    'URY': {
        'adolescent': False,
        'id': 19,
        'mcc': 748,
        'name': u'Uruguay',
        'ratingsbody': 'ESRB',
        'slug': 'uy',
        'special': False,
        'weight': 0
    },
    'USA': {
        'adolescent': True,
        'id': 2,
        'mcc': 310,
        'name': u'United States',
        'ratingsbody': 'ESRB',
        'slug': 'us',
        'special': False,
        'weight': 1
    },
    'UZB': {
        'adolescent': True,
        'id': 243,
        'name': u'Uzbekistan',
        'ratingsbody': None,
        'slug': 'uz',
        'special': False,
        'weight': 0
    },
    'VAT': {
        'adolescent': True,
        'id': 134,
        'name': u'Holy See',
        'ratingsbody': None,
        'slug': 'va',
        'special': False,
        'weight': 0
    },
    'VCT': {
        'adolescent': True,
        'id': 205,
        'name': u'Saint Vincent and the Grenadines',
        'ratingsbody': None,
        'slug': 'vc',
        'special': False,
        'weight': 0
    },
    'VEN': {
        'adolescent': False,
        'id': 10,
        'mcc': 734,
        'name': u'Venezuela',
        'ratingsbody': 'ESRB',
        'slug': 've',
        'special': False,
        'weight': 0
    },
    'VGB': {
        'adolescent': True,
        'id': 245,
        'name': u'Virgin Islands, British',
        'ratingsbody': None,
        'slug': 'vg',
        'special': False,
        'weight': 0
    },
    'VIR': {
        'adolescent': True,
        'id': 246,
        'name': u'Virgin Islands, U.S.',
        'ratingsbody': None,
        'slug': 'vi',
        'special': False,
        'weight': 0
    },
    'VNM': {
        'adolescent': True,
        'id': 244,
        'name': u'Viet Nam',
        'ratingsbody': None,
        'slug': 'vn',
        'special': False,
        'weight': 0
    },
    'VUT': {
        'adolescent': True,
        'id': 47,
        'mcc': 541,
        'name': u'Vanuatu',
        'slug': 'vu',
        'special': False,
        'weight': 0
    },
    'WLF': {
        'adolescent': True,
        'id': 247,
        'name': u'Wallis and Futuna',
        'ratingsbody': None,
        'slug': 'wf',
        'special': False,
        'weight': 0
    },
    'WSM': {
        'adolescent': True,
        'id': 206,
        'name': u'Samoa',
        'ratingsbody': None,
        'slug': 'ws',
        'special': False,
        'weight': 0
    },
    'YEM': {
        'adolescent': True,
        'id': 249,
        'name': u'Yemen',
        'ratingsbody': None,
        'slug': 'ye',
        'special': False,
        'weight': 0
    },
    'ZAF': {
        'adolescent': True,
        'id': 37,
        'mcc': 655,
        'name': u'South Africa',
        'ratingsbody': None,
        'slug': 'za',
        'special': False,
        'weight': 0
    },
    'ZMB': {
        'adolescent': True,
        'id': 250,
        'name': u'Zambia',
        'ratingsbody': None,
        'slug': 'zm',
        'special': False,
        'weight': 0
    },
    'ZWE': {
        'adolescent': True,
        'id': 251,
        'name': u'Zimbabwe',
        'ratingsbody': None,
        'slug': 'zw',
        'special': False,
        'weight': 0
    },
}
