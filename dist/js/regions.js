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
    return {"REGION_CHOICES_SLUG": {"gt": gettext('Guatemala'), "co": gettext('Colombia'), "cn": gettext('China'), "cl": gettext('Chile'), "za": gettext('South Africa'), "ec": gettext('Ecuador'), "cz": gettext('Czech Republic'), "ar": gettext('Argentina'), "in": gettext('Indonesia'), "cr": gettext('Costa Rica'), "es": gettext('Spain'), "ve": gettext('Venezuela'), "ni": gettext('Nicaragua'), "rs": gettext('Serbia'), "pa": gettext('Panama'), "restofworld": gettext('Rest of World'), "pe": gettext('Peru'), "it": gettext('Italy'), "ph": gettext('Philippines'), "pl": gettext('Poland'), "bd": gettext('Bangladesh'), "fr": gettext('France'), "ru": gettext('Russia'), "de": gettext('Germany'), "jp": gettext('Japan'), "hu": gettext('Hungary'), "br": gettext('Brazil'), "gr": gettext('Greece'), "me": gettext('Montenegro'), "uy": gettext('Uruguay'), "sv": gettext('El Salvador'), "us": gettext('United States'), "uk": gettext('United Kingdom'), "mx": gettext('Mexico')}};
}));
