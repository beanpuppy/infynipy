from infynipy.models.group import ReferrerGroup
from .. import IntegrationTest, vcrr


class TestReferrerGroup(IntegrationTest):

    @vcrr.use_cassette
    def test_referrer_group_get_multiple(self):
        for group in self.infynity.referrer_groups:
            assert isinstance(group, ReferrerGroup)

    @vcrr.use_cassette
    def test_referrer_group_create(self):
        data = {
            "group_name": "Test3 Group",
            "broker_id": 20041
        }

        group_id = self.infynity.referrer_group(data=data).create()
        assert isinstance(group_id, str)
