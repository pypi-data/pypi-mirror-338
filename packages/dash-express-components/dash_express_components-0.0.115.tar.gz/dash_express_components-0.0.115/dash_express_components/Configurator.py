# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Configurator(Component):
    """A Configurator component.
<div style="width:450px; margin-left: 20px; float: right;  margin-top: -150px;">
<img src="https://raw.githubusercontent.com/VK/dash-express-components/main/.media/configurator.png"/>
</div>


The configurator component helps to define plot definitions based on the
metadata of a dataframe.
Different configuration parts like `Filter`, `Transform` or `Plotter`
are combined in a single accordion component.

The metadata is used to compute the available parameters after data 
transformations and newly available colums are adjusted automatically.

@hideconstructor

@example
import dash_express_components as dxc
import plotly.express as px

meta = dxc.get_meta(px.data.gapminder())

 dxc.Configurator(
          id="plotConfig",
          meta=meta,
 )
@public

Keyword arguments:

- id (string; required):
    The ID used to identify this component in Dash callbacks. @type
    {string}.

- config (boolean | number | string | dict | list; optional):
    The resulting configuration of the plot. @type {Object}.

- currentConfig (boolean | number | string | dict | list; optional):
    The current configuration of the plot. @type {Object}.

- meta (boolean | number | string | dict | list; required):
    The metadata the plotter selection is based on. @type {Object}.

- showFilter (boolean; default True):
    Prop to define the visibility of the Filter panel @type {boolean}.

- showMetadata (boolean; default False):
    Prop to define the visibility of the Metadata panel @type
    {boolean}.

- showParameterization (boolean; default False):
    Prop to define the visibility of the Parameterization panel @type
    {boolean}.

- showPlotter (boolean; default True):
    Prop to define the visibility of the Plot panel @type {boolean}.

- showStore (boolean; default False):
    Prop to define the visibility of the Store panel @type {boolean}.

- showTransform (boolean; default True):
    Prop to define the visibility of the Transform panel @type
    {boolean}.

- showUpdate (boolean; default True):
    Prop to define the visibility of the update plot button @type
    {boolean}."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_express_components'
    _type = 'Configurator'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        meta: typing.Optional[typing.Any] = None,
        config: typing.Optional[typing.Any] = None,
        currentConfig: typing.Optional[typing.Any] = None,
        showFilter: typing.Optional[bool] = None,
        showTransform: typing.Optional[bool] = None,
        showPlotter: typing.Optional[bool] = None,
        showMetadata: typing.Optional[bool] = None,
        showParameterization: typing.Optional[bool] = None,
        showStore: typing.Optional[bool] = None,
        showUpdate: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'config', 'currentConfig', 'meta', 'showFilter', 'showMetadata', 'showParameterization', 'showPlotter', 'showStore', 'showTransform', 'showUpdate']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'config', 'currentConfig', 'meta', 'showFilter', 'showMetadata', 'showParameterization', 'showPlotter', 'showStore', 'showTransform', 'showUpdate']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'meta']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Configurator, self).__init__(**args)
