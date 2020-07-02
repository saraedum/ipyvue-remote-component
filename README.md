# ipyvue-remote-component

Load Vue components for ipyvue at runtime with vue-remote-component.

## Installation

### Classical Jupyter Notebook

Install with pip:

    $ pip install ipyvue_remote_component
    $ jupyter nbextension enable --py --sys-prefix ipyvue_remote_component

### Jupyter Lab

Make sure that you have the `@jupyter-widgets/jupyterlab-manager` installed:

    $ jupyter labextension install @jupyter-widgets/jupyterlab-manager

Install with pip:

    $ pip install ipyvue_remote_component
    $ jupyter labextension install ipyvue_remote_component

### Development with the Jupyter Notebook

Build JavaScript assets:

    $ cd src/typescript
    $ yarn build:notebook

Then, install with pip:

    $ cd ../python
    $ pip install -e .

Enable the extension:

    $ jupyter nbextension install --py --symlink --sys-prefix ipyvue_remote_component
    $ jupyter nbextension enable --py --sys-prefix ipyvue_remote_component

The Python bits should now update automatically when you restart the kernel, to
update the JavaScript, run `yarn build notebook` again, or `yarn build notebook
--watch` to rebuild automatically.

### Development with Jupyter Lab

Make sure that you have the `@jupyter-widgets/jupyterlab-manager` installed:

    $ jupyter labextension install @jupyter-widgets/jupyterlab-manager

Build JavaScript assets and install the JupyterLab extension:

    $ cd src/typescript
    $ yarn build:jupyterlab
    $ jupyter labextension install .

Then, install the Python backend with pip:

    $ cd ../python
    $ pip install -e .

To rebuild the frontend code automatically, run `yarn build jupyterlab
--watch`. To have JupyterLab rebuild whenever that frontend build changes,
start JupyterLab with `--watch`.
