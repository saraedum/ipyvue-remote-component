from .remote_component import RemoteComponent


version_info = (1, 1, 1)
__version__ = "1.1.1"


def _jupyter_labextension_paths():
    r"""
    Called by JupyterLab to find out which JavaScript assets need to be copied.
    """
    # The command `jupyter labextension build` creates a package in
    # labextension/, see jupyterlab.outputDir in js/package.json
    # These files are copied to extensions/ipyvue-remote-component/ in
    # JupyterLab when this package is pip-installed.
    return [{
        'src': 'labextension',
        'dest': 'ipyvue-remote-component',
    }]


def _jupyter_nbextension_paths():
    r"""
    Called by Jupyter Notebook to find out which JavaScript assets need to be copied.
    """
    # The command `yarn build:prod` creates JavaScript assets in nbextension/.
    # These files need to be copied to the nbextensions/ipyvue-remote-component
    # directory in Jupyter Notebook. The entrypoint in these files is
    # extension.js.
    return [{
        'section': 'notebook',
        'src': 'nbextension',
        'dest': 'ipyvue-remote-component',
        'require': 'ipyvue-remote-component/extension'
    }]
