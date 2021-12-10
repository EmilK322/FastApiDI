import pytest


class TestFastApiDependencyRegistry:
    @pytest.mark.skip(reason='not sure how to test it, it has only one line of private attribute use')
    def test_to_dependency_overrides(self):
        assert False
