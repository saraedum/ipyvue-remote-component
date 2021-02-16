from traitlets import Any
from ipywidgets import DOMWidget
from ipywidgets.widgets.widget import widget_serialization

from .force_load import force_load

class RemoteComponent(DOMWidget):
    r"""
    A base class for VueTemplates that makes sure that the <remote-component>
    tag is supported.
    
    All this does is reference a model in the ipyvue-remote-component so the
    extension is loaded in the frontend.  When using this as a base class, you
    still need to inherit from VueTemplate or some other ipyvue base.
    """
    __force = Any(force_load, read_only=True).tag(sync=True, **widget_serialization)
