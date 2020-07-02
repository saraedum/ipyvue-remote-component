def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        # used when --symlink installing to determine the source of JavaScript assets
        'src': '../generated/notebook/javascript/',
        # src is linked/copied to share/jupyter/nbextensions/<dest>/
        'dest': 'ipyvue-remote-component',
        # entrypoint of the notebook extension in share/jupyter/nbextensions/
        'require': 'ipyvue-remote-component/extension'
    }]

