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
    return {"COLLECTION_COLORS": {"amber": "#cc440d", "topaz": "#ffb300", "amethyst": "#7a3675", "sapphire": "#2d457e", "emerald": "#1b8215", "aquamarine": "#197b99", "garnet": "#cc3388", "ruby": "#c93333"}};
}));
