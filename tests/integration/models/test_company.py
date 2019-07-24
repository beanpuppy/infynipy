import pytest
from infynipy.models.company import Company
from infynipy.models.entity.address import Address
from .. import IntegrationTest, vcrr


class TestCompany(IntegrationTest):

    @vcrr.use_cassette
    def test_companies_get(self):
        for company in self.infynity.broker(int(pytest.placeholders.broker_id)).companies:
            assert isinstance(company, Company)

    @vcrr.use_cassette
    def test_companies_get_addresses(self):
        company = self.infynity.broker(int(pytest.placeholders.broker_id)).companies[0]

        for address in company.addresses:
            assert isinstance(address, Address)
