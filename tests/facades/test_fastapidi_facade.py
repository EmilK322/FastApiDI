from unittest import mock

from fastapidi.facades import FastApiDI


class TestFastApiDI:
    def test_init_with_app_set_dependency_overrides_provider(self) -> None:
        # arrange
        fastapi_app_mock = mock.MagicMock()

        # act
        app_di = FastApiDI(fastapi_app_mock)

        # assert
        assert fastapi_app_mock.router.dependency_overrides_provider is app_di

    def test_dependency_overrides_property_returns_dict(self) -> None:
        # arrange
        fastapi_app_mock = mock.MagicMock()
        app_di = FastApiDI(fastapi_app_mock)

        # act
        dependency_overrides = app_di.dependency_overrides

        # assert
        assert isinstance(dependency_overrides, dict)
