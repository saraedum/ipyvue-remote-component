const plugin = require('./plugin');
const base = require('@jupyter-widgets/base');

module.exports = {
  id: 'ipyvue-remote-component:plugin',
  requires: [base.IJupyterWidgetRegistry],
  activate: function(app, widgets) {
      plugin.activate(app, widgets);
      widgets.registerWidget({
          name: 'ipyvue-remote-component',
          version: plugin.version,
          exports: plugin,
      });
  },
  autoStart: true
};
