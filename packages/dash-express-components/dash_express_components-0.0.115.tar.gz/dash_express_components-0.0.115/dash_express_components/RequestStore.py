# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class RequestStore(Component):
    """A RequestStore component.
Easily keep data on the client side with this component.
The data is not inserted in the DOM.
Data can be in memory, localStorage or sessionStorage.
The data will be kept with the id as key.
The data will be collected from the url with additional info from the config
We use a longCallback feature, if set

Keyword arguments:

- id (string; required)

- clear_data (boolean; default False)

- config (dict; optional)

- data (dict | list | number | string | boolean; optional)

- longCallback (boolean; default False)

- modified_timestamp (number; default -1)

- storage_type (a value equal to: 'local', 'session', 'memory'; default 'memory')

- url (string; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_express_components'
    _type = 'RequestStore'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        storage_type: typing.Optional[Literal["local", "session", "memory"]] = None,
        data: typing.Optional[typing.Union[dict, typing.Sequence, typing.Union[int, float, numbers.Number], str, bool]] = None,
        clear_data: typing.Optional[bool] = None,
        modified_timestamp: typing.Optional[typing.Union[int, float, numbers.Number]] = None,
        url: typing.Optional[str] = None,
        config: typing.Optional[dict] = None,
        longCallback: typing.Optional[bool] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'clear_data', 'config', 'data', 'longCallback', 'modified_timestamp', 'storage_type', 'url']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'clear_data', 'config', 'data', 'longCallback', 'modified_timestamp', 'storage_type', 'url']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(RequestStore, self).__init__(**args)
