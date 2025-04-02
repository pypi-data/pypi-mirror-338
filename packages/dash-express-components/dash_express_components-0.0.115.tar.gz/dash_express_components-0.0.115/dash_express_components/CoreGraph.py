# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class CoreGraph(Component):
    """A CoreGraph component.
CoreGraph just wraps the Graph of dash_core_components.

Keyword arguments:

- id (optional):
    The ID of this component, used to identify dash components in
    callbacks. The ID needs to be unique across all of the components
    in an app. @type {string}.

- figure (default {    data: [],    layout: {},    frames: [],}):
    Plotly `figure` object. See schema:
    https://plotly.com/javascript/reference  `config` is set
    separately by the `config` property."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_express_components'
    _type = 'CoreGraph'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        figure: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'figure']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'figure']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(CoreGraph, self).__init__(**args)
