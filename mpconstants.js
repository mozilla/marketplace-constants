var fs = require('fs');


module.exports = function(file) {
  return require('./dist/js/' + file);
};
