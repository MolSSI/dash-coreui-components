# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class approuteconditional(Component):
    """An approuteconditional component.
Route conditional component.

This component (and its children) are only visible if the browser's current URL matches its route prop.
This provides a light-weight client-side alternative to the server-side routing described in https://dash.plot.ly/urls.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children.
- id (string; default 'approuteconditional'): The ID used to identify this component in Dash callbacks, defaults to `approuteconditional`.
- route (string; required): The route. This component is only visible if the browser's current URL matches the contents of this prop.
- className (string; optional): The CSS class name, defaults to `route-conditional`.
- tag (string; default 'div'): The HTML tag, defaults to `div`."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, route=Component.REQUIRED, className=Component.UNDEFINED, tag=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'route', 'className', 'tag']
        self._type = 'approuteconditional'
        self._namespace = 'dcc'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'route', 'className', 'tag']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['route']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(approuteconditional, self).__init__(children=children, **args)
