from importlib import import_module


def get_region(locale):
    locale = locale.replace('-', '_')
    locales = [locale, 'en_US']
    if '_' in locale:
        # Add in a fallback so it goes: zh-CN, zh, en-US
        locales.insert(1, locale.split('_')[0])
    mod = None
    for locale in locales:
        try:
            mod = import_module('.' + locale, 'mpconstants.regions')
            break
        except ImportError:
            pass
    else:
        raise IOError('Failed to find locales: {0}'.format(locales))
    return mod
