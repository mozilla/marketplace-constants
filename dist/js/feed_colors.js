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
    return {"FEED_COLORS": {"amber": "#F78813", "garnet": "#A20D55", "topaz": "#0099D0", "amethyst": "#5A197E", "sapphire": "#1E1E9C", "emerald": "#00953F", "ruby": "#CE001C"}};
}));
