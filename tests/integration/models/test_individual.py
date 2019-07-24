import pytest
from infynipy.models.individual import Individual
from infynipy.models.entity.address import Address
from infynipy.models.entity.employment import Employment
from infynipy.models.entity.income import Income
from infynipy.models.entity.expense import Expense
from infynipy.models.entity.liability import Liability
from infynipy.models.entity.asset import Asset
from .. import IntegrationTest, vcrr


class TestIndividual(IntegrationTest):

    @vcrr.use_cassette
    def test_individuals_get(self):
        for individual in self.infynity.broker(int(pytest.placeholders.broker_id)).individuals:
            assert isinstance(individual, Individual)

    @vcrr.use_cassette
    def test_individuals_get_addresses(self):
        individual = self.infynity.broker(int(pytest.placeholders.broker_id)).individuals[2]

        for address in individual.addresses:
            assert isinstance(address, Address)

    @vcrr.use_cassette
    def test_individuals_get_employments(self):
        individual = self.infynity.broker(int(pytest.placeholders.broker_id)).individuals[2]

        for employment in individual.employments:
            assert isinstance(employment, Employment)

    @vcrr.use_cassette
    def test_individuals_create_address(self):
        new_address_data = {
            "address_standard": "Standard",
            "non_std_address_line": "",
            "building_name": "",
            "floor_number": "",
            "unit_number": "",
            "street_number": "645",
            "street_name": "Jumbuk Road",
            "street_type": "",
            "city": "Yinnar South",
            "state": "VIC",
            "postcode": "3869",
            "country": "Australia",
            "po_box_type": "",
            "po_box": "",
        }

        individual = self.infynity.broker(int(pytest.placeholders.broker_id)).individuals[2]
        individual.new_address('PreSettlementResidential', new_address_data)

    @vcrr.use_cassette
    def test_individuals_create_employment(self):
        new_employment_data = {
            "occupation": "422111",
            "started": "2019-06-19",
            "ended": None,
            "current": "Current",
            "type": "PAYE",
            "sector": "Public",
            "status": "Full Time",
            "acting_for_trust": False,
            "abn": "0",
            "gst_registered": True,
            "company_acn": "0",
            "company_contact_name": "Jim Pickens",
            "company_contact_title": "Mr.",
            "company_email": "",
            "company_fax_area_code": "02",
            "company_fax_number": "411752009",
            "company_mobile_phone": None,
            "company_name": "Johnson and Johnson",
            "company_phone_number": "111111111",
            "company_phone_area_code": "02",
        }

        individual = self.infynity.broker(int(pytest.placeholders.broker_id)).individuals[0]
        individual.employment(data=new_employment_data).create()

    @vcrr.use_cassette
    def test_individuals_get_incomes(self):
        individual = self.infynity.broker(int(pytest.placeholders.broker_id)).individuals[2]

        for income in individual.incomes:
            assert isinstance(income, Income)

    @vcrr.use_cassette
    def test_individuals_get_liabilities(self):
        individual = self.infynity.broker(int(pytest.placeholders.broker_id)).individuals[2]

        for liability in individual.liabilities:
            assert isinstance(liability, Liability)

    @vcrr.use_cassette
    def test_individuals_get_assets(self):
        individual = self.infynity.broker(int(pytest.placeholders.broker_id)).individuals[2]

        for asset in individual.assets:
            assert isinstance(asset, Asset)

    @vcrr.use_cassette
    def test_individuals_get_expenses(self):
        individual = self.infynity.broker(int(pytest.placeholders.broker_id)).individuals[2]

        for expense in individual.expenses:
            assert isinstance(expense, Expense)
