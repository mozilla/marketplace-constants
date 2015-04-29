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
    return {"MOBILE_CODES": {"740": "ec", "605": "tn", "748": "uy", "712": "cr", "602": "eg", "704": "gt", "334": "mx", "311": "us", "310": "us", "608": "sn", "404": "in", "202": "gr", "440": "jp", "234": "uk", "235": "uk", "250": "ru", "230": "cz", "624": "cm", "470": "bd", "222": "it", "316": "us", "730": "cl", "214": "es", "541": "vu", "652": "bw", "734": "ve", "208": "fr", "466": "tw", "706": "sv", "313": "us", "632": "gw", "714": "pa", "612": "ci", "716": "pe", "610": "ml", "611": "gn", "460": "cn", "614": "ne", "617": "mu", "262": "de", "246": "lt", "405": "in", "655": "za", "710": "ni", "724": "br", "623": "cf", "220": "rs", "732": "co", "414": "mm", "640": "tz", "416": "jo", "260": "pl", "722": "ar", "216": "hu", "646": "mg", "441": "jp", "297": "me", "515": "ph", "639": "ke"}, "REGION_CHOICES_SLUG": {"gw": gettext("Guinea-Bissau"), "ci": gettext("C\u00f4te d'Ivoire"), "gt": gettext("Guatemala"), "co": gettext("Colombia"), "cn": gettext("China"), "cm": gettext("Cameroon"), "cl": gettext("Chile"), "eg": gettext("Egypt"), "in": gettext("India"), "za": gettext("South Africa"), "ec": gettext("Ecuador"), "cz": gettext("Czech Republic"), "ar": gettext("Argentina"), "vu": gettext("Vanuatu"), "cr": gettext("Costa Rica"), "gn": gettext("Guinea-Conakry"), "es": gettext("Spain"), "ve": gettext("Venezuela"), "ni": gettext("Nicaragua"), "tz": gettext("Tanzania"), "rs": gettext("Serbia"), "tw": gettext("Taiwan"), "ne": gettext("Niger"), "tn": gettext("Tunisia"), "lt": gettext("Lithuania"), "pa": gettext("Panama"), "restofworld": gettext("Rest of World"), "pe": gettext("Peru"), "it": gettext("Italy"), "ph": gettext("Philippines"), "pl": gettext("Poland"), "bd": gettext("Bangladesh"), "fr": gettext("France"), "ru": gettext("Russia"), "de": gettext("Germany"), "jp": gettext("Japan"), "cf": gettext("Central African Republic"), "jo": gettext("Jordan"), "br": gettext("Brazil"), "hu": gettext("Hungary"), "gr": gettext("Greece"), "me": gettext("Montenegro"), "mg": gettext("Madagascar"), "uy": gettext("Uruguay"), "ke": gettext("Kenya"), "mm": gettext("Myanmar"), "ml": gettext("Mali"), "sv": gettext("El Salvador"), "us": gettext("United States"), "mu": gettext("Mauritius"), "bw": gettext("Botswana"), "sn": gettext("Senegal"), "uk": gettext("United Kingdom"), "mx": gettext("Mexico")}};
}));
