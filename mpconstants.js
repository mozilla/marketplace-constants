var fs = require('fs');


module.exports = function(file) {
  return JSON.parse(fs.readFileSync(__dirname + '/assets/js/' + file + '.json'));
};
