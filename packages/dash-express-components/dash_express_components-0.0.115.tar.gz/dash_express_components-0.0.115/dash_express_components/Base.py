# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class Base(Component):
    """A Base component.


Keyword arguments:

- id (optional):
    The ID used to identify this component in Dash callbacks.

- config (optional):
    The config the user sets in this component.

- meta (optional):
    The metadata this section is based on.

- meta_out (optional):
    The metadata section will create as output.

- setProps (optional):
    Dash-assigned callback that should be called to report property
    changes to Dash, to make them available for callbacks."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_express_components'
    _type = 'Base'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        config: typing.Optional[typing.Any] = None,
        meta: typing.Optional[typing.Any] = None,
        meta_out: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'config', 'meta', 'meta_out', 'setProps']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'config', 'meta', 'meta_out', 'setProps']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        super(Base, self).__init__(**args)
