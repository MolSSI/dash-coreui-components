# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class appsidebar(Component):
    """An appsidebar component.
CoreUI sidebar component.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children, supports `appsidebarfooter`, `appsidebarform`, `appsidebarheader`, `appsidebarminimizer`, and `appsidebarnav`.
- id (string; default 'appsidebar'): The ID used to identify this component in Dash callbacks, defaults to `appsidebar`.
- className (string; optional): The CSS class name, defaults to `sidebar`.
- compact (boolean; default False): The compact flag, defaults to `false`.
- display (string; default ''): The display bootstrap class.
- fixed (boolean; default False): The fixed flag, defaults to `false`.
- minimized (boolean; default False): The minimized flag, defaults to `false`.
- isOpen (boolean; default False): The isOpen flag, defaults to `false`.
- offCanvas (boolean; default False): The offCanvas flag, defaults to `false`.
- staticContext (boolean | number | string | dict | list; optional): TODO document this.
- tag (string; default 'div'): The HTML tag, defaults to `div`."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, compact=Component.UNDEFINED, display=Component.UNDEFINED, fixed=Component.UNDEFINED, minimized=Component.UNDEFINED, isOpen=Component.UNDEFINED, offCanvas=Component.UNDEFINED, staticContext=Component.UNDEFINED, tag=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'compact', 'display', 'fixed', 'minimized', 'isOpen', 'offCanvas', 'staticContext', 'tag']
        self._type = 'appsidebar'
        self._namespace = 'dcc'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'compact', 'display', 'fixed', 'minimized', 'isOpen', 'offCanvas', 'staticContext', 'tag']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(appsidebar, self).__init__(children=children, **args)
