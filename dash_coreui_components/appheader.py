# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class appheader(Component):
    """An appheader component.
CoreUI header component.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children.
- id (string; default 'appheader'): The ID used to identify this component in Dash callbacks, defaults to `appheader`.
- className (string; optional): The CSS class name.
- fixed (boolean; default False): Wether the header is fixed, defaults to `false`.
- tag (string; default 'header'): The HTML tag, defaults to `header`."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, fixed=Component.UNDEFINED, tag=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'fixed', 'tag']
        self._type = 'appheader'
        self._namespace = 'dash_coreui_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'fixed', 'tag']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(appheader, self).__init__(children=children, **args)
