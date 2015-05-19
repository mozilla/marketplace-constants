(function(root, factory) {
    if (typeof define === 'function' && define.amd) {
        // AMD. Register as an anonymous module.
        define([], factory);
    } else if (typeof exports === 'object') {
        // Node. Does not work with strict CommonJS, but
        // only CommonJS-like environments that support module.exports,
        // like Node.
        module.exports = factory();
    } else {
        // Browser globals (root is window).
        root.returnExports = factory();
    }
}(this, function() {
    return {"CARRIER_SLUGS": ["megafon", "kddi", "vimpelcom", "deutsche_telekom", "sprint", "o2", "tmn", "america_movil", "congstar", "telenor", "singtel", "telefonica", "orange", "etisalat", "grameenphone", "china_unicom", "mtn", "qtel", "telecom_italia_group", "smart", "hutchinson_three_group", "kt"], "MOBILE_CODES": {"260": {"2": "deutsche_telekom"}, "214": {"5": "telefonica", "7": "telefonica"}, "262": {"1": {"__default": "deutsche_telekom", "congstar.de": "congstar", "congstar": "congstar"}, "2": "deutsche_telekom", "7": "o2"}, "541": {"1": "orange"}, "297": {"1": "telenor", "2": "deutsche_telekom", "4": "deutsche_telekom"}, "310": {"160": "deutsche_telekom", "26": "deutsche_telekom", "260": "deutsche_telekom", "490": "deutsche_telekom"}, "334": {"2": "america_movil", "3": "telefonica", "20": "america_movil"}, "740": {"1": "america_movil"}, "602": {"1": "orange"}, "605": {"1": "orange"}, "608": {"1": "orange"}, "610": {"2": "orange"}, "611": {"1": "orange"}, "612": {"3": "orange"}, "614": {"4": "orange"}, "617": {"1": "orange"}, "623": {"3": "orange"}, "624": {"2": "orange"}, "632": {"3": "orange"}, "639": {"7": "orange"}, "640": {"2": "orange"}, "646": {"2": "orange"}, "652": {"2": "orange"}, "655": {"10": "mtn"}, "416": {"77": "orange"}, "440": {"75": "kddi", "70": "kddi", "7": "kddi", "8": "kddi", "73": "kddi", "74": "kddi", "71": "kddi", "76": "kddi", "77": "kddi", "78": "kddi", "79": "kddi", "72": "kddi", "50": "kddi", "51": "kddi", "52": "kddi", "53": "kddi", "54": "kddi", "55": "kddi", "56": "kddi", "88": "kddi", "89": "kddi"}, "714": {"2": "telefonica", "3": "america_movil"}, "704": {"3": "telefonica"}, "706": {"4": "telefonica"}, "710": {"3": "telefonica"}, "712": {"4": "telefonica"}, "716": {"10": "america_movil", "6": "telefonica"}, "202": {"5": "deutsche_telekom"}, "460": {"1": "china_unicom"}, "722": {"320": "america_movil", "10": "telefonica", "330": "america_movil", "310": "america_movil", "70": "telefonica"}, "724": {"10": "telefonica", "11": "telefonica", "6": "telefonica", "23": "telefonica"}, "470": {"1": "grameenphone"}, "216": {"1": "telenor", "20": "telenor", "70": "deutsche_telekom", "30": "deutsche_telekom"}, "730": {"2": "telefonica"}, "220": {"1": "telenor", "2": "telenor"}, "734": {"4": "telefonica"}, "732": {"123": "telefonica", "102": "telefonica"}, "230": {"1": "deutsche_telekom", "2": "telefonica", "10": "telefonica"}, "234": {"2": "telefonica", "11": "telefonica", "10": "telefonica", "30": "deutsche_telekom"}, "748": {"10": "america_movil", "7": "telefonica"}}};
}));
