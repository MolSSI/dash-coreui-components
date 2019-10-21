# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class apptablebody(Component):
    """An apptablebody component.


Keyword arguments:
- children (a list of or a singular dash component, string or number; optional)
- id (string; default 'tablebody')
- className (string; optional)
- tag (string; default 'tr')
- style (dict; optional)
- data (boolean | number | string | dict | list; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, tag=Component.UNDEFINED, style=Component.UNDEFINED, data=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'tag', 'style', 'data']
        self._type = 'apptablebody'
        self._namespace = 'dash_coreui_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'tag', 'style', 'data']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(apptablebody, self).__init__(children=children, **args)
