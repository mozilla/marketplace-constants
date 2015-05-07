# -*- coding: utf8 -*-

CARRIER_DETAILS = {
    'UNKNOWN_CARRIER': {
        # Used as a dummy.
        'id': 0,
        'name': '',
        'slug': 'carrierless',
    },
    'TELEFONICA': {
        'id': 1,
        'name': u'Telefónica',
        'slug': 'telefonica',
    },
    'AMERICA_MOVIL': {
        'id': 2,
        'name': u'América Móvil',
        'slug': 'america_movil',
    },
    'CHINA_UNICOM': {
        'id': 3,
        'name': u'China Unicom',
        'slug': 'china_unicom',
    },
    'DEUTSCHE_TELEKOM': {
        'id': 4,
        'name': u'Deutsche Telekom',
        'slug': 'deutsche_telekom',
    },
    'ETISALAT': {
        'id': 5,
        'name': u'Etisalat',
        'slug': 'etisalat',
    },
    'HUTCHINSON_THREE_GROUP': {
        'id': 6,
        'name': u'Hutchinson Three Group',
        'slug': 'hutchinson_three_group',
    },
    'KDDI': {
        'id': 7,
        'name': u'KDDI',
        'slug': 'kddi',
    },
    'KT': {
        'id': 8,
        'name': u'KT',
        'slug': 'kt',
    },
    'MEGAFON': {
        'id': 9,
        'name': u'MegaFon',
        'slug': 'megafon',
    },
    'QTEL': {
        'id': 10,
        'name': u'Qtel',
        'slug': 'qtel',
    },
    'SINGTEL': {
        'id': 11,
        'name': u'SingTel',
        'slug': 'singtel',
    },
    'SMART': {
        'id': 12,
        'name': u'Smart',
        'slug': 'smart',
    },
    'SPRINT': {
        'id': 13,
        'name': u'Sprint',
        'slug': 'sprint',
    },
    'TELECOM_ITALIA_GROUP': {
        'id': 14,
        'name': u'Telecom Italia Group',
        'slug': 'telecom_italia_group',
    },
    'TELENOR': {
        'id': 15,
        'name': u'Telenor',
        'slug': 'telenor',
    },
    'TMN': {
        'id': 16,
        'name': u'TMN',
        'slug': 'tmn',
    },
    'VIMPELCOM': {
        'id': 17,
        'name': u'VimpelCom',
        'slug': 'vimpelcom',
    },
    'GRAMEENPHONE': {
        'id': 18,
        'name': 'GrameenPhone',
        'slug': 'grameenphone',
    },
    'CONGSTAR': {
        'id': 19,
        'name': u'Congstar',
        'slug': 'congstar',
    },
    'O2': {
        'id': 20,
        'name': u'O2',
        'slug': 'o2',
    },
    'MTN': {
        'id': 21,
        'name': u'MTN',
        'slug': 'mtn',
    },
    'ORANGE': {
        'id': 22,
        'name': u'Orange',
        'slug': 'orange',
    }
}

MOBILE_CODES = {
    # Greece
    202: {
        # This is Cosmote, but our contract is with DT, the owner
        5: 'deutsche_telekom'
    },

    # Spain
    214: {
        5: 'telefonica',
        7: 'telefonica'
    },

    # Hungary
    216: {
        1: 'telenor',
        20: 'telenor',
        30: 'deutsche_telekom',
        # Actually Vodafone but treat like DT.
        70: 'deutsche_telekom'
    },

    # Serbia
    220: {
        1: 'telenor',
        2: 'telenor'
    },

    # Czech Republic
    230: {
        1: 'deutsche_telekom',
        2: 'telefonica',
        10: 'telefonica'
    },

    # United Kingdom
    234: {
        2: 'telefonica',
        10: 'telefonica',
        11: 'telefonica',
        30: 'deutsche_telekom'
    },

    # Poland
    260: {
        2: 'deutsche_telekom'
    },

    # Germany
    262: {
        1: {
            # Differentiate congstar using the SPN, everything else with
            # that MNC is DT.
            '__default': 'deutsche_telekom',
            'congstar': 'congstar',
            'congstar.de': 'congstar'
        },
        2: 'deutsche_telekom',
        7: 'o2'
    },

    # Montenegro
    297: {
        1: 'telenor',
        2: 'deutsche_telekom',
        4: 'deutsche_telekom'
    },

    # United States
    # T-Mobile has a bunch of other MNCs but they are marked as
    # 'Not Operational' on http:#en.wikipedia.org/wiki/Mobile_country_code
    310: {
        26: 'deutsche_telekom',
        160: 'deutsche_telekom',
        260: 'deutsche_telekom',
        490: 'deutsche_telekom'
    },

    # Mexico
    334: {
        2: 'america_movil',
        3: 'telefonica',
        20: 'america_movil'
    },

    # Jordan
    416: {
        77: 'orange'
    },

    # Japan
    440: {
        7: 'kddi',
        8: 'kddi',
        50: 'kddi',
        51: 'kddi',
        52: 'kddi',
        53: 'kddi',
        54: 'kddi',
        55: 'kddi',
        56: 'kddi',
        70: 'kddi',
        71: 'kddi',
        72: 'kddi',
        73: 'kddi',
        74: 'kddi',
        75: 'kddi',
        76: 'kddi',
        77: 'kddi',
        78: 'kddi',
        79: 'kddi',
        88: 'kddi',
        89: 'kddi'
    },

    # China
    460: {
        1: 'china_unicom'
    },

    # Bangladesh
    470: {
        1: 'grameenphone'
    },

    # Vanuatu
    541: {
        1: 'orange'
    },

    # Egypt
    602: {
        1: 'orange'
    },

    # Tunisia
    605: {
        1: 'orange'
    },

    # Senegal
    608: {
        1: 'orange'
    },

    # Mali
    610: {
        2: 'orange'
    },

    # Guinea-Conakry
    611: {
        1: 'orange'
    },

    # Côte d'Ivoire
    612: {
        3: 'orange'
    },

    # Niger
    614: {
        4: 'orange'
    },

    # Mauritius
    617: {
        1: 'orange'
    },

    # Central African Republic
    623: {
        3: 'orange'
    },

    # Cameroon
    624: {
        2: 'orange'
    },

    # Guinea Bissau
    632: {
        3: 'orange'
    },

    # Kenya
    639: {
        7: 'orange'
    },

    # Tanzania
    640: {
        2: 'orange'
    },

    # Madagascar
    646: {
        2: 'orange'
    },

    # Botswana
    652: {
        2: 'orange'
    },

    # South Africa
    655: {
        10: 'mtn'
    },

    # Guatemala
    704: {
        3: 'telefonica'
    },

    # El Salvador
    706: {
        4: 'telefonica'
    },

    # Nicaragua
    710: {
        3: 'telefonica'
    },

    # Costa Rica
    712: {
        4: 'telefonica'
    },

    # Panama
    714: {
        2: 'telefonica',
        3: 'america_movil'
    },

    # Peru
    716: {
        6: 'telefonica',
        10: 'america_movil'
    },

    # Argentina
    722: {
        10: 'telefonica',
        70: 'telefonica',
        # Claro
        310: 'america_movil',
        320: 'america_movil',
        330: 'america_movil'
    },

    # Brazil
    724: {
        6: 'telefonica',
        10: 'telefonica',
        11: 'telefonica',
        23: 'telefonica'
    },

    # Chile
    730: {
        2: 'telefonica'
    },

    # Colombia
    732: {
        102: 'telefonica',
        123: 'telefonica'
    },

    # Venezuela
    734: {
        4: 'telefonica'
    },

    # Ecuador
    740: {
        1: 'america_movil'
    },

    # Uruguay
    748: {
        7: 'telefonica',
        # Claro.
        10: 'america_movil'
    }
}

CARRIER_SLUGS = [_carrier['slug'] for _carrier in CARRIER_DETAILS.values()]
