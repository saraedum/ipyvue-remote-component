var path = require('path');
var version = require('./package.json').version;

var rules = [
    { test: /\.css$/, use: ['style-loader', 'css-loader']}
]

// Note that unfortunately, we cannot declare "vue" an external. JupyterVue
// bundles all of Vue but does not export all of it again for us. (Not sure if
// that would even be possible.) So we have to include our own copy.
// (Otherwise, RequireJS would try to load vue from extensions/vue.js which
// does not exist.

module.exports = (env, argv) => {
    var devtool = argv.mode === 'development' ? 'source-map' : false;
    return [
        {// Notebook extension
        //
        // This bundle only contains the part of the JavaScript that is run on
        // load of the notebook. This section generally only performs
        // some configuration for requirejs, and provides the legacy
        // "load_ipython_extension" function which is required for any notebook
        // extension.
        //
            entry: './lib/extension.js',
            output: {
                filename: 'extension.js',
                path: path.resolve(__dirname, '..', 'ipyvue_remote_component', 'nbextension'),
                libraryTarget: 'amd',
                publicPath: '' // publicPath is set in extension.js
            },
            devtool,
            externals: ['jupyter-vue'],
        },
        {// Bundle for the notebook containing the custom widget views and models
        //
        // This bundle contains the implementation for the custom widget views and
        // custom widget.
        // It must be an amd module
        //
            entry: './lib/index.js',
            output: {
                filename: 'index.js',
                path: path.resolve(__dirname, '..', 'ipyvue_remote_component', 'nbextension'),
                libraryTarget: 'amd',
                publicPath: '',
            },
            devtool,
            module: {
                rules: rules
            },
            externals: ['@jupyter-widgets/base', 'jupyter-vue'],
        },
        {// Embeddable ipyvue-remote-component bundle
        //
        // This bundle is generally almost identical to the notebook bundle
        // containing the custom widget views and models.
        //
        // The only difference is in the configuration of the webpack public path
        // for the static assets.
        //
        // It will be automatically distributed by unpkg to work with the static
        // widget embedder.
        //
        // The target bundle is always `dist/index.js`, which is the path required
        // by the custom widget embedder.
        //
            entry: './lib/index.js',
            output: {
                filename: 'index.js',
                path: path.resolve(__dirname, 'dist'),
                libraryTarget: 'amd',
                publicPath: 'https://unpkg.com/ipyvue-remote-component@' + version + '/dist/'
            },
            devtool,
            module: {
                rules: rules
            },
            externals: ['@jupyter-widgets/base', 'jupyter-vue'],
        }
    ];
}
