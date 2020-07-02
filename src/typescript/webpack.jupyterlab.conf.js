var path = require('path');
var widget = require('./webpack.notebook.conf.js')[1];

const plugin = {
    // This bundle contains the frontend of the JupyterLab plugin. We
    // precompile this into an AMD bundle which is then picked up by JupyterLab
    // which recompiles it into its actual bundle.
    // We do not use JupyterLab bundling directly since we want to have full
    // control over the build process.
    entry: './ipyvue-remote-component/jupyterlab/plugin.ts',
    output: {
        path: path.resolve(__dirname, "dist", "jupyterlab"),
        filename: "index.js",
        libraryTarget: "amd"
    },
    devtool: "eval-source-map",
    externals: [
        /^@lumino\/.+$/,
        /^@jupyterlab\/.+$/,
        '@jupyter-widgets/base',
        'vue',
    ],
    module: widget.module,
    plugins: widget.plugins,
}

module.exports = [ plugin ];
