from infynipy import Infynity


class UnitTest:
    """Base class for Infynipy unit tests."""

    def setup(self):
        """Setup runs before all test cases."""
        # self.infynity = Infynity(username="dummy", api_key="dummy")
        self.infynity = Infynity(username="beanpup_py", api_key="9f8fec7407134befb00462fe550ba270")
