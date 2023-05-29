from vlogs.sdk import VLogs, VLogsOptions
from vlogs.model import Collector, CollectorType, CollectorSource

appId = "72bd14c306a91fa8a590330e3898ddcc"
apiKey = "vlogs_gX9WwSdKatMNdpUClLU0IfCx575tvdoeQ"

# Create VLogs instance
sdk = VLogs.create(
    VLogsOptions.builder()
    .apiKey(apiKey)
    .appId(appId)
    .build()
)

response = sdk.collect(
    Collector.builder()
    .type(CollectorType.Error)
    .source(CollectorSource.Other)
    .message("This is a test message")
    .build()
)

print("Response: ", response)