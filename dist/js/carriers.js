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
    return {"CARRIER_SLUGS": ["megafon", "kddi", "vimpelcom", "deutsche_telekom", "sprint", "o2", "tmn", "america_movil", "congstar", "telenor", "singtel", "telefonica", "orange", "etisalat", "grameenphone", "china_unicom", "mtn", "qtel", "telecom_italia_group", "smart", "hutchinson_three_group", "kt"]};
}));
