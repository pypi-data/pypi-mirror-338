# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Imshow(Component):
    """An Imshow component.


Keyword arguments:

- allColOptions (optional):
    All currently available column options.

- catColOptions (optional):
    Currently available categorical options.

- config (optional):
    The config the user sets in this component.

- numColOptions (optional):
    Currently available numerical options.

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes to Dash, to make them available for callbacks."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_express_components'
    _type = 'Imshow'

    @_explicitize_args
    def __init__(
        self,
        config: typing.Optional[typing.Any] = None,
        allColOptions: typing.Optional[typing.Any] = None,
        catColOptions: typing.Optional[typing.Any] = None,
        numColOptions: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['allColOptions', 'catColOptions', 'config', 'numColOptions', 'setProps']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['allColOptions', 'catColOptions', 'config', 'numColOptions', 'setProps']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Imshow, self).__init__(**args)
