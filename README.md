ipyvue-remote-component
===============================

Load Vue.js Component Packages at Runtime in Jupyter Notebooks and JupyterLab

Installation
------------

To install use pip:

    $ pip install ipyvue_remote_component

For a development installation (requires [Node.js](https://nodejs.org) and [Yarn version 1](https://classic.yarnpkg.com/)),

    $ git clone https://github.com/saraedum/ipyvue-remote-component.git
    $ cd ipyvue-remote-component
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --overwrite --sys-prefix ipyvue_remote_component
    $ jupyter nbextension enable --py --sys-prefix ipyvue_remote_component

When actively developing your extension for JupyterLab, run the command:

    $ jupyter labextension develop --overwrite ipyvue_remote_component

Then you need to rebuild the JS when you make a code change:

    $ cd js
    $ yarn run build

You then need to refresh the JupyterLab page when your javascript changes.
