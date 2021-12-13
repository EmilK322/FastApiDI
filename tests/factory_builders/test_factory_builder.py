from typing import List, Dict, Any
from unittest import mock
from unittest.mock import call

import pytest

from FastApiDI.factory_builders import FactoryBuilder


class TestFactoryBuilder:
    @pytest.mark.parametrize('args,kwargs', [
        ([], {}),
        ([1, 6, 'qwe', 8.6, float], {}),
        ([], {'a': 'asd', 'qwe': 'dgh'}),
        ([1, 6, 'qwe', 8.6, float], {'a': 'asd', 'qwe': 6})
    ])
    def test_create_scoped_with_callable_return_factory_of_return_type_of_callable(self, args: List, kwargs: Dict) -> None:
        # arrange
        factory_builder = FactoryBuilder()
        callable_object_mock = mock.MagicMock()
        object_mock = mock.MagicMock()
        callable_object_mock.return_value = object_mock

        # act
        returned_factory = factory_builder.create_scoped(callable_object_mock, *args, **kwargs)
        returned_object = returned_factory()

        # assert
        assert returned_object is object_mock
        callable_object_mock.assert_called_once_with(*args, **kwargs)

    def test_create_scoped_call_factory_many_times_calls_callable_each_time(self) -> None:
        # arrange
        calls_number = 10
        factory_builder = FactoryBuilder()
        callable_object_mock = mock.MagicMock()
        calls = [call() for _ in range(calls_number)]

        # act
        returned_factory = factory_builder.create_scoped(callable_object_mock)
        [returned_factory() for _ in range(calls_number)]

        # assert
        callable_object_mock.assert_has_calls(calls)

    @pytest.mark.parametrize('args,kwargs', [
        ([], {}),
        ([1, 6, 'qwe', 8.6, float], {}),
        ([], {'a': 'asd', 'qwe': 'dgh'}),
        ([1, 6, 'qwe', 8.6, float], {'a': 'asd', 'qwe': 6})
    ])
    def test_create_singleton_with_callable_return_factory_of_return_type_of_callable(self, args: List, kwargs: Dict) -> None:
        # arrange
        factory_builder = FactoryBuilder()
        callable_object_mock = mock.MagicMock()
        object_mock = mock.MagicMock()
        callable_object_mock.return_value = object_mock

        # act
        returned_factory = factory_builder.create_singleton(callable_object_mock, *args, **kwargs)
        returned_object = returned_factory()

        # assert
        assert returned_object is object_mock
        callable_object_mock.assert_called_once_with(*args, **kwargs)

    def test_create_singleton_call_factory_many_times_calls_callable_single_time(self) -> None:
        # arrange
        calls_number = 10
        factory_builder = FactoryBuilder()
        callable_object_mock = mock.MagicMock()
        calls = call()

        # act
        returned_factory = factory_builder.create_scoped(callable_object_mock)
        [returned_factory() for _ in range(calls_number)]

        # assert
        callable_object_mock.assert_has_calls(calls)