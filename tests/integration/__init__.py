r"""Integration test suite"""
import re
import pytest
import vcr
from infynipy import Infynity


def scrub_numerical_ids(request):
    # Removes any numerical ids from the uri
    # E.g 'https://api.infynity.com.au/v1/individual/1337'
    #  -> 'https://api.infynity.com.au/v1/individual/<ID>'
    request.uri = re.sub('\d{2,}', '<ID>', request.uri)
    return request

vcrr = vcr.VCR(
    cassette_library_dir='tests/integration/cassettes',
    record_mode='once',
    filter_headers=['authorization'],
    before_record_request=scrub_numerical_ids,
    match_on=['uri', 'method'],
)


class IntegrationTest:
    """Base class for infynipy integration tests"""

    def setup(self):
        self.infynity = Infynity(
            username=pytest.placeholders.username,
            api_key=pytest.placeholders.api_key,
        )
