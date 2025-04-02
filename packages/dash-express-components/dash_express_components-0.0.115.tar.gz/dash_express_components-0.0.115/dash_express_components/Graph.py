# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401

import os
dash_url_base_pathname = os.environ.get("DASH_URL_BASE_PATHNAME", "/")
dash_base_plot_api = os.environ.get("DASH_EXPRESS_PLOTAPI", "plotApi")
if dash_base_plot_api != "":
    defaultPlotApi = dash_url_base_pathname + dash_base_plot_api
else:
    defaultPlotApi = ""
                 


from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Graph(Component):
    """A Graph component.
<div style="width:450px; margin-left: 20px; float: right;  margin-top: -150px;">
<img src="https://raw.githubusercontent.com/VK/dash-express-components/main/.media/graph.png"/>
<img src="https://raw.githubusercontent.com/VK/dash-express-components/main/.media/graph-table.png"/>
<img src="https://raw.githubusercontent.com/VK/dash-express-components/main/.media/graph-modal.png"/>
</div>


The `Graph` component is a combination of the original dash `Graph` and the dash `data_table`.

It can not only be used to render a plotly.js-powered data visualization,
but also shows a searchable table, if only data is submitted.

In addition, there is the possibility to add plot parameters as `defParams` and 
the dataframe `meta` data.  
This automatically adds a configurator modal, which can be opened via a button
at the bottom right.


@hideconstructor

@example
import dash_express_components as dxc
import plotly.express as px

meta = dxc.get_meta(px.data.gapminder())

dxc.Graph(
    id="fig",
    meta=meta,
    defParams={}
)
@public

Keyword arguments:

- id (string; required):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app. @type {string}.

- className (string; default ""):
    className of the parent div.

- currentConfig (boolean | number | string | dict | list; optional):
    The current configuration of the plot. @type {Object}.

- defParams (dict; optional):
    Configuration to describe the plot features.

- editButton (boolean; default True):
    enable/disable edit button.

- figure (boolean | number | string | dict | list; default {    data: [],    layout: {},    frames: [],}):
    Plotly `figure` object. See schema:
    https://plotly.com/javascript/reference  `config` is set
    separately by the `config` property.

- hiddenColumns (list; default ["_id", "index"]):
    hidden column names (array of strings).

- longCallback (boolean; default False):
    enable/disable long callbacks.

- meta (boolean | number | string | dict | list; optional):
    The metadata the plotter selection is based on.

- plotApi (string; default ""):
    Url to the plot Api.

- saveClick (boolean; default False):
    enable/disable saveClick button.

- selectedData (boolean | number | string | dict | list; optional):
    The data selected in the plot or in the table.

- showFilter (boolean; default True):
    Prop to define the visibility of the Filter panel @type {boolean}.

- showTransform (boolean; default True):
    Prop to define the visibility of the Transform panel @type
    {boolean}."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_express_components'
    _type = 'Graph'
        # with plotApiPatch

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        defParams: typing.Optional[dict] = None,
        meta: typing.Optional[typing.Any] = None,
        plotApi: typing.Optional[str] = None,
        figure: typing.Optional[typing.Any] = None,
        style: typing.Optional[typing.Any] = None,
        selectedData: typing.Optional[typing.Any] = None,
        className: typing.Optional[str] = None,
        saveClick: typing.Optional[bool] = None,
        longCallback: typing.Optional[bool] = None,
        editButton: typing.Optional[bool] = None,
        currentConfig: typing.Optional[typing.Any] = None,
        showFilter: typing.Optional[bool] = None,
        showTransform: typing.Optional[bool] = None,
        hiddenColumns: typing.Optional[typing.Sequence] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'className', 'currentConfig', 'defParams', 'editButton', 'figure', 'hiddenColumns', 'longCallback', 'meta', 'plotApi', 'saveClick', 'selectedData', 'showFilter', 'showTransform', 'style']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'currentConfig', 'defParams', 'editButton', 'figure', 'hiddenColumns', 'longCallback', 'meta', 'plotApi', 'saveClick', 'selectedData', 'showFilter', 'showTransform', 'style']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Graph, self).__init__(**args)

        if not hasattr(self, "plotApi") and defaultPlotApi != "":
            setattr(self, "plotApi", defaultPlotApi)
                 