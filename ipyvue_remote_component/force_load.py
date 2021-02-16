from traitlets import Unicode
from ipywidgets import DOMWidget

class ForceLoad(DOMWidget):
    r"""
    RemoteComponent includes this widget to force the `activate()` function in
    the JavaScript part of ipyvue-remote-component to run.

    We need this to make sure that the `<remote-component/>` component gets
    registered with Vue.js before any Vue code gets rendered by ipyvue.
    """
    _model_name = Unicode('ForceLoadModel').tag(sync=True)
    _model_module = Unicode('ipyvue-remote-component').tag(sync=True)
    _model_module_version = Unicode('^1.0.0').tag(sync=True)

force_load = ForceLoad()
