from vlogs.model import Collector, CollectorSource, CollectorType
from vlogs.sdk import VLogs, VLogsOptions
from vlogs.util import generate_uuid
import pytest

appId = "72bd14c306a91fa8a590330e3898ddcc"
apiKey = "vlogs_gX9WwSdKatMNdpUClLU0IfCx575tvdoeQ"

# Create VLogs instance
sdk = VLogs.create(
    VLogsOptions.builder()
    .apiKey(apiKey)
    .appId(appId)
    .build()
)


def test_create():
    assert sdk is not None
    assert sdk._options is not None
    assert sdk._options.appId == appId
    assert sdk._options.apiKey == apiKey


def test_generate_uuid():
    assert generate_uuid() != generate_uuid()


def test_collect():
    request = Collector.builder().type(CollectorType.Error).source(
        CollectorSource.Other).message("This is a test message from vlogs python sdk").build()
    response = sdk.collect(request)

    assert response.id is not None
    assert response.id != ""
    assert response.id == request.id
    assert response.message == "ok"


@pytest.mark.asyncio
async def test_collect_async():
    request = Collector.builder().type(CollectorType.Error).source(
        CollectorSource.Other).message("This is a test message from vlogs python sdk with async function").build()
    response = await sdk.collect_async(request)

    assert response.id is not None
    assert response.id != ""
    assert response.id == request.id
    assert response.message == "ok"
