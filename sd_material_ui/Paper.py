# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Paper(Component):
    """A Paper component.
A Dash material-ui Paper component

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): Can be used to render elements inside the Paper
- id (string; optional): ID for Paper
- className (string; optional): The CSS class name of the root element
- classes (dict; optional): The classes to be applied to this component. This keys in this object must be valid CSS rule
names, and the values must be strings for the classnames to be assigned to each rule name
Valid rule names are:
  root
  rounded
  outlined
  elevation0
  elevation1
  ...
  elevation23
  elevation24. classes has the following type: dict containing keys 'root', 'rounded', 'outlined', 'elevation0', 'elevation1'.
  Those keys have the following types:
  - root (string; optional)
  - rounded (string; optional)
  - outlined (string; optional)
  - elevation0 (string; required)
  - elevation1 (string; required)
- rounded (boolean; default True): By default, the paper container will have a border radius.
Set this to false to generate a container with sharp corners.
- style (dict; optional): Override the inline-styles of the root element
- zDepth (number; default 1): This number represents the zDepth of the paper shadow"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, classes=Component.UNDEFINED, rounded=Component.UNDEFINED, style=Component.UNDEFINED, zDepth=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'className', 'classes', 'rounded', 'style', 'zDepth']
        self._type = 'Paper'
        self._namespace = 'sd_material_ui'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'className', 'classes', 'rounded', 'style', 'zDepth']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Paper, self).__init__(children=children, **args)
