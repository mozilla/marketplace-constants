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

CARRIER_SLUGS = [_carrier['slug'] for _carrier in CARRIER_DETAILS.values()]
