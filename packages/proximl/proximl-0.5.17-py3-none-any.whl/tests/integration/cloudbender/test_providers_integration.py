import re
import sys
import asyncio
from pytest import mark, fixture

pytestmark = [mark.sdk, mark.integration, mark.cloudbender, mark.providers]


@mark.create
@mark.asyncio
@mark.xdist_group("cloudbender_resources")
class GetProviderTests:
    async def test_get_providers(self, proximl, provider):
        providers = await proximl.cloudbender.providers.list()
        assert len(providers) > 0

    async def test_get_provider(self, proximl, provider):
        response = await proximl.cloudbender.providers.get(provider.id)
        assert response.id == provider.id

    async def test_provider_properties(self, provider):
        assert isinstance(provider.id, str)
        assert isinstance(provider.type, str)
        assert provider.type == "test"
        assert provider.credits == 0

    async def test_provider_str(self, provider):
        string = str(provider)
        regex = r"^{.*\"provider_uuid\": \"" + provider.id + r"\".*}$"
        assert isinstance(string, str)
        assert re.match(regex, string)

    async def test_provider_repr(self, provider):
        string = repr(provider)
        regex = (
            r"^Provider\( proximl , \*\*{.*'provider_uuid': '"
            + provider.id
            + r"'.*}\)$"
        )
        assert isinstance(string, str)
        assert re.match(regex, string)
