# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class ConfigReceiver(Component):
    """A ConfigReceiver component.
A config receiver listening for `window.postMessage()`

@hideconstructor

@example
 rec = dxc.ConfigReceiver(
          id="plotConfig",
          token="test"
 )

 window.postMessage({config: "Test", token:"test" })
@public

Keyword arguments:

- id (string; required):
    The ID used to identify this component in Dash callbacks. @type
    {string}.

- config (boolean | number | string | dict | list; optional):
    Prop The resulting configuration of the plot. @type {Object}.

- token (string; required):
    A token used to define the configuration across frames. @type
    {string}."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_express_components'
    _type = 'ConfigReceiver'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        token: typing.Optional[str] = None,
        config: typing.Optional[typing.Any] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'config', 'token']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'config', 'token']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id', 'token']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(ConfigReceiver, self).__init__(**args)
