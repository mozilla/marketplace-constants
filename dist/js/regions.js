(function(root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define(['core/l10n'], factory);
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
    return {"MOBILE_CODES": {"740": "ec", "605": "tn", "214": "es", "712": "cr", "602": "eg", "748": "uy", "334": "mx", "311": "us", "310": "us", "608": "sn", "404": "in", "440": "jp", "234": "uk", "235": "uk", "250": "ru", "230": "cz", "624": "cm", "470": "bd", "222": "it", "316": "us", "730": "cl", "405": "in", "541": "vu", "652": "bw", "734": "ve", "208": "fr", "706": "sv", "610": "ml", "313": "us", "632": "gw", "202": "gr", "612": "ci", "716": "pe", "704": "gt", "714": "pa", "460": "cn", "614": "ne", "617": "mu", "262": "de", "246": "lt", "655": "za", "710": "ni", "724": "br", "220": "rs", "732": "co", "414": "mm", "640": "tz", "416": "jo", "260": "pl", "722": "ar", "216": "hu", "646": "mg", "441": "jp", "297": "me", "515": "ph"}, "REGION_CHOICES_SLUG": {"gw": gettext("Guinea-Bissau"), "ci": gettext("C\u00f4te d'Ivoire"), "gt": gettext("Guatemala"), "co": gettext("Colombia"), "cn": gettext("China"), "cm": gettext("Cameroon"), "cl": gettext("Chile"), "eg": gettext("Egypt"), "za": gettext("South Africa"), "ec": gettext("Ecuador"), "cz": gettext("Czech Republic"), "ar": gettext("Argentina"), "vu": gettext("Vanuatu"), "in": gettext("India"), "cr": gettext("Costa Rica"), "es": gettext("Spain"), "ve": gettext("Venezuela"), "ni": gettext("Nicaragua"), "tz": gettext("Tanzania"), "rs": gettext("Serbia"), "ne": gettext("Niger"), "tn": gettext("Tunisia"), "lt": gettext("Lithuania"), "pa": gettext("Panama"), "restofworld": gettext("Rest of World"), "pe": gettext("Peru"), "it": gettext("Italy"), "ph": gettext("Philippines"), "pl": gettext("Poland"), "bd": gettext("Bangladesh"), "fr": gettext("France"), "ru": gettext("Russia"), "de": gettext("Germany"), "jp": gettext("Japan"), "hu": gettext("Hungary"), "jo": gettext("Jordan"), "br": gettext("Brazil"), "gr": gettext("Greece"), "me": gettext("Montenegro"), "mg": gettext("Madagascar"), "uy": gettext("Uruguay"), "mm": gettext("Myanmar"), "ml": gettext("Mali"), "sv": gettext("El Salvador"), "us": gettext("United States"), "mu": gettext("Mauritius"), "bw": gettext("Botswana"), "sn": gettext("Senegal"), "uk": gettext("United Kingdom"), "mx": gettext("Mexico")}};
}));
