# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Tabs(Component):
    """A Tabs component.
Material UI Tabs component

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): Pass Tab components as children
- id (string; default ''): Element ID
- className (string; optional): CSS class name of the root element
- style (dict; optional): Override the inline-styles of the root element
- tabPropsArray (list; optional): Array of tab properties. Available props:
classes
disabled
disableRipple
disableFocusRipple
icon
label
value
wrapped
- value (bool | number | str | dict | list; default False): Makes Tabs controllable and selects the tab whose value prop matches this prop"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, fireEvent=Component.UNDEFINED, style=Component.UNDEFINED, tabPropsArray=Component.UNDEFINED, value=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'style', 'tabPropsArray', 'value']
        self._type = 'Tabs'
        self._namespace = 'sd_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'style', 'tabPropsArray', 'value']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Tabs, self).__init__(children=children, **args)
