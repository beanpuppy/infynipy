from infynipy.models.referrer import Referrer
from .. import IntegrationTest, vcrr


class TestReferrer(IntegrationTest):

    @vcrr.use_cassette
    def test_referrer_get_multiple(self):
        for referrer in self.infynity.referrers:
            assert isinstance(referrer, Referrer)

    @vcrr.use_cassette
    def test_referrer_create(self):
        data = {
            "broker_id": 20041,
            "name": "Referme Ayy",
            "phone": "041234566",
            "mobile": "0487985642",
            "email": "test@test.com",
            "account_name": "Test Account Name",
            "bank_name": "ANZ",
            "bsb": "032456",
            "account_number": "12345678",
            "abn": "12345678",
            "gst_registered": "yes",
            "company_name": "Test"
        }

        referrer_id = self.infynity.referrer(data=data).create()
        assert isinstance(referrer_id, str)
