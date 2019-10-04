# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class appsidebarform(Component):
    """An appsidebarform component.
CoreUI sidebar form component.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children.
- id (string; default 'appsidebarform'): The ID used to identify this component in Dash callbacks, defaults to `appsidebarform`.
- className (string; optional): The CSS class name, defaults to `sidebar-form`.
- tag (string; default 'div'): The HTML tag, defaults to `div`."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, tag=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'tag']
        self._type = 'appsidebarform'
        self._namespace = 'dcc'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'tag']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(appsidebarform, self).__init__(children=children, **args)
