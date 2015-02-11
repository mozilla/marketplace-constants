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
    return {"COLLECTION_COLORS": {"amber": "#ED8040", "garnet": "#E77286", "amethyst": "#8D4B87", "sapphire": "#3A5990", "emerald": "#8BC873", "aquamarine": "#00C9A8", "ruby": "#D46952"}};
}));
