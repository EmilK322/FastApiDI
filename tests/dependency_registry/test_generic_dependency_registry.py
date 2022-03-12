from unittest import mock

import pytest

from fastapidi.dependency_registry import GenericDependencyRegistry


class TestGenericDependencyRegistry:
    @pytest.fixture
    def generic_dependency_registry(self):
        return GenericDependencyRegistry

    @pytest.mark.parametrize('dependency,implementation,args,kwargs',[
        ('dep', 'impl', [], {}),
        ('dep', 'impl', [1,'2', int], {'1': 1, 'asd': 'qwe', '6': float}),
        (int, float, [3], {}),
        (sum, max, [1, 7, 9, 3], {})
    ])
    def test_register_singleton(self, dependency, implementation, args, kwargs):
        # arrange
        factory_builder_mock = mock.MagicMock()
        generic_dependency_registry = GenericDependencyRegistry(factory_builder_mock)

        # act
        generic_dependency_registry.register_singleton(dependency, implementation, *args, **kwargs)

        # assert
        factory_builder_mock.create_singleton.assert_called_once_with(implementation, *args, **kwargs)


    @pytest.mark.parametrize('dependency,implementation,args,kwargs', [
        ('dep', 'impl', [], {}),
        ('dep', 'impl', [1, '2', int], {'1': 1, 'asd': 'qwe', '6': float}),
        (int, float, [3], {}),
        (sum, max, [1, 7, 9, 3], {})
    ])
    def test_register_scoped(self, dependency, implementation, args, kwargs):
        # arrange
        factory_builder_mock = mock.MagicMock()
        generic_dependency_registry = GenericDependencyRegistry(factory_builder_mock)

        # act
        generic_dependency_registry.register_scoped(dependency, implementation, *args, **kwargs)

        # assert
        factory_builder_mock.create_scoped.assert_called_once_with(implementation, *args, **kwargs)

    @pytest.mark.skip(reason='not sure how to test it, it has only one line of private attribute use')
    def test_register_factory(self):
        assert False

    @pytest.mark.skip(reason='not sure how to test it, it has only one line of private attribute use')
    def test_get_dependency_factory(self):
        assert False


