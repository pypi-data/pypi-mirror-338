# AUTO GENERATED FILE - DO NOT EDIT

import typing  # noqa: F401
import numbers # noqa: F401
from typing_extensions import TypedDict, NotRequired, Literal # noqa: F401
from dash.development.base_component import Component, _explicitize_args
try:
    from dash.development.base_component import ComponentType # noqa: F401
except ImportError:
    ComponentType = typing.TypeVar("ComponentType", bound=Component)


class DataGraph(Component):
    """A DataGraph component.


Keyword arguments:

- id (string; required)

- data (dict; default { "no_data": [1, 2, 3] })

- defParams (dict; optional)"""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_express_components'
    _type = 'DataGraph'

    @_explicitize_args
    def __init__(
        self,
        id: typing.Optional[typing.Union[str, dict]] = None,
        defParams: typing.Optional[dict] = None,
        data: typing.Optional[dict] = None,
        **kwargs
    ):
        self._prop_names = ['id', 'data', 'defParams']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'data', 'defParams']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')

        super(DataGraph, self).__init__(**args)
