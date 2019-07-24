from infynipy import Infynity
from . import UnitTest


class TestInfynity(UnitTest):

    def test_build(self):
        assert isinstance(self.infynity, Infynity)
