# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class PlotterBase(Component):
    """A PlotterBase component.


Keyword arguments:

- id (optional):
    The config the user sets in this component.

- allColOptions (optional):
    All currently available column options.

- catColOptions (optional):
    Currently available categorical options.

- config (optional):
    The config the user sets in this component.

- numColOptions (optional):
    Currently available numerical options.

- numOptions (optional):
    Currently available options without grouping.

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes to Dash, to make them available for callbacks."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_express_components'
    _type = 'PlotterBase'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        config: typing.Optional[typing.Any] = None,
        allColOptions: typing.Optional[typing.Any] = None,
        catColOptions: typing.Optional[typing.Any] = None,
        numColOptions: typing.Optional[typing.Any] = None,
        numOptions: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'allColOptions', 'catColOptions', 'config', 'numColOptions', 'numOptions', 'setProps']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'allColOptions', 'catColOptions', 'config', 'numColOptions', 'numOptions', 'setProps']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(PlotterBase, self).__init__(**args)
