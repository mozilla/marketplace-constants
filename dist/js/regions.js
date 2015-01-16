(function(root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define(['l10n'], factory);
    } else if (typeof exports === 'object') {
        // Node. Does not work with strict CommonJS, but
        // only CommonJS-like environments that support module.exports,
        // like Node.
        module.exports = factory();
    } else {
        // Browser globals (root is window).
        root.returnExports = factory();
    }
}(this, function(l10n) {
    var gettext = function(str) {
        return str;
    };
    if (l10n) {
        var gettext = l10n.gettext;
    }
    return {"MOBILE_CODES": {"216": "hu", "740": "ec", "214": "es", "704": "gt", "334": "mx", "311": "us", "310": "us", "316": "us", "404": "in", "440": "jp", "748": "uy", "234": "uk", "235": "uk", "250": "ru", "230": "cz", "730": "cl", "724": "br", "313": "us", "405": "in", "732": "co", "734": "ve", "716": "pe", "706": "sv", "202": "gr", "208": "fr", "441": "jp", "714": "pa", "712": "cr", "460": "cn", "262": "de", "260": "pl", "655": "za", "710": "ni", "222": "it", "220": "rs", "470": "bd", "722": "ar", "297": "me", "515": "ph"}, "REGION_CHOICES_SLUG": {"gt": gettext('Guatemala'), "co": gettext('Colombia'), "cn": gettext('China'), "cl": gettext('Chile'), "za": gettext('South Africa'), "ec": gettext('Ecuador'), "cz": gettext('Czech Republic'), "ar": gettext('Argentina'), "in": gettext('India'), "cr": gettext('Costa Rica'), "es": gettext('Spain'), "ve": gettext('Venezuela'), "ni": gettext('Nicaragua'), "rs": gettext('Serbia'), "pa": gettext('Panama'), "restofworld": gettext('Rest of World'), "pe": gettext('Peru'), "it": gettext('Italy'), "ph": gettext('Philippines'), "pl": gettext('Poland'), "bd": gettext('Bangladesh'), "fr": gettext('France'), "ru": gettext('Russia'), "de": gettext('Germany'), "jp": gettext('Japan'), "hu": gettext('Hungary'), "br": gettext('Brazil'), "gr": gettext('Greece'), "me": gettext('Montenegro'), "uy": gettext('Uruguay'), "sv": gettext('El Salvador'), "us": gettext('United States'), "uk": gettext('United Kingdom'), "mx": gettext('Mexico')}};
}));
