module.exports = {
  ...require('./force-load-model.js'),
  version: require('../package.json').version,
}

require('./activate.js')['activate']()
