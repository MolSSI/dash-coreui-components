# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class appheaderdropdown(Component):
    """An appheaderdropdown component.
CoreUI header dropdown menu component.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children.
- id (string; default 'appheaderdropdown'): The ID used to identify this component in Dash callbacks, defaults to `appheaderdropdown`.
- direction (string; default 'down'): The dropdown direction, defaults to `down`."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, direction=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'direction']
        self._type = 'appheaderdropdown'
        self._namespace = 'dash_coreui_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'direction']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(appheaderdropdown, self).__init__(children=children, **args)
