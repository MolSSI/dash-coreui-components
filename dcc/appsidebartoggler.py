# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class appsidebartoggler(Component):
    """An appsidebartoggler component.
CoreUI sidebar toggler component.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children, defaults to  `<span className="navbar-toggler-icon" />`.
- id (string; default 'appsidebartoggler'): The ID used to identify this component in Dash callbacks, defaults to `appsidebartoggler`.
- className (string; optional): The CSS class name, defaults to `navbar-toggler`.
- display (boolean | number | string | dict | list; default 'lg'): The display bootstrap class, defaults to `lg`.
- mobile (boolean; default False): The mobile mode flag, default to `false`.
- tag (string; default 'button'): The HTML tag, defaults to `button`.
- type (string; default 'button'): The HTML type, defauls to `button`."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, display=Component.UNDEFINED, mobile=Component.UNDEFINED, tag=Component.UNDEFINED, type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'display', 'mobile', 'tag', 'type']
        self._type = 'appsidebartoggler'
        self._namespace = 'dcc'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'display', 'mobile', 'tag', 'type']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(appsidebartoggler, self).__init__(children=children, **args)
