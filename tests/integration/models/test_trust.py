import pytest
from infynipy.models.trust import Trust
from infynipy.models.entity.address import Address
from .. import IntegrationTest, vcrr


class TestTrust(IntegrationTest):

    @vcrr.use_cassette
    def test_trusts_get(self):
        for trust in self.infynity.broker(int(pytest.placeholders.broker_id)).trusts:
            assert isinstance(trust, Trust)

    @vcrr.use_cassette
    def test_trusts_get_addresses(self):
        trust = self.infynity.broker(int(pytest.placeholders.broker_id)).trusts[0]

        for address in trust.addresses:
            assert isinstance(address, Address)
