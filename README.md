ipyvue-remote-component
=======================

Load Vue.js Packages at Runtime in Jupyter Notebooks and JupyterLab

Installation
------------

To install use pip:

    pip install ipyvue_remote_component

Development
-----------

The more interesting bits of this package live in a separate JavaScript package
called [vue-remote-component](https://github.com/saraedum/vue-remote-component).
What's here is, except for the `ForceLoad` hack, just generic boilerplate from
the [widget-cookiecutter](https://github.com/jupyter-widgets/widget-cookiecutter).

To use a development version of `vue-remote-component` you might want to `yarn
link` your local copy of `vue-remote-component` in the `js/` directory.

Otherwise, to only work on the bits that are exposed here:

    git clone https://github.com/saraedum/ipyvue-remote-component.git
    cd ipyvue-remote-component
    pip install -e .

When working with the classical notebook:

    jupyter nbextension install --py --symlink --overwrite --sys-prefix ipyvue_remote_component
    jupyter nbextension enable --py --sys-prefix ipyvue_remote_component

When working with JupyterLab:

    jupyter labextension develop --overwrite ipyvue_remote_component

To rebuild the JavaScript code after making changes to `vue-remote-component`
or anything in the `js/` directory:

    cd js
    yarn run build
    cd ..
    pip install -e . --no-deps

You then need to refresh the Notebook/JupyterLab page when your javascript changes.
