# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Plotter(Component):
    """A Plotter component.
<div style="width:450px; margin-left: 20px; float: right;  margin-top: -150px;">
<img src="https://raw.githubusercontent.com/VK/dash-express-components/main/.media/plotter.png"/>
<img src="https://raw.githubusercontent.com/VK/dash-express-components/main/.media/plotter-modal.png"/>
</div>

The `Plotter` component helps to define the right plot parameters in the style of plotly.express.

There are several different plot types, and some of them are given directly by plotly.express, like:
<ul style="margin-left: 20px;">
  <li>scatter</li>
  <li>box</li>
  <li>violin</li>
  <li>bar</li>
  <li>scatter_matrix</li>
</ul>

Others are computed more indirect, like:
<ul style="margin-left: 20px;">
  <li>imshow</li>
  <li>bar_count</li>
  <li>histogram_line</li>
  <li>probability</li>
  <li>table</li>
</ul>

@hideconstructor

@example
import dash_express_components as dxc
import plotly.express as px

meta = dxc.get_meta(px.data.gapminder())

dxc.Plotter(
???
)
@public

Keyword arguments:

- id (string; required):
    The ID used to identify this component in Dash callbacks.

- config (boolean | number | string | dict | list; optional):
    The config the user sets in this component.

- meta (boolean | number | string | dict | list; required):
    The metadata this section is based on.

- meta_out (boolean | number | string | dict | list; optional):
    The metadata section will create as output."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_express_components'
    _type = 'Plotter'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        config: typing.Optional[typing.Any] = None,
        meta: typing.Optional[typing.Any] = None,
        meta_out: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'config', 'meta', 'meta_out']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'config', 'meta', 'meta_out']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'meta']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(Plotter, self).__init__(**args)
