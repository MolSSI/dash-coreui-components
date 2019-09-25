# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class appnavbarbrand(Component):
    """An appnavbarbrand component.
CoreUI navbar brand component.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children, defaults to `<img src width height alt className/>`.
- tag (string; default 'a'): The HTML tag, defaults to `a`.
- id (string; default 'appnavbarbrand'): The ID used to identify this component in Dash callbacks, defaults to `appnavbarbrand`.
- className (string; optional): The CSS class name, defaults to `navbar-brand`.
- brand (boolean | number | string | dict | list; optional): The brand image, given as `{src, width, height, alt, className: 'navbar-brand' }`.
- full (boolean | number | string | dict | list; optional): The full size brand image, given as `{src, width, height, alt, className: 'navbar-brand-full' }`.
- minimized (boolean | number | string | dict | list; optional): The minimized brand image, given as `{src, width, height, alt, className: 'navbar-brand-minimized' }`."""
    @_explicitize_args
    def __init__(self, children=None, tag=Component.UNDEFINED, id=Component.UNDEFINED, className=Component.UNDEFINED, brand=Component.UNDEFINED, full=Component.UNDEFINED, minimized=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'tag', 'id', 'className', 'brand', 'full', 'minimized']
        self._type = 'appnavbarbrand'
        self._namespace = 'dcc'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'tag', 'id', 'className', 'brand', 'full', 'minimized']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(appnavbarbrand, self).__init__(children=children, **args)
