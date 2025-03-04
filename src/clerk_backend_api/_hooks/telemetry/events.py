from typing import Optional, Any

EVENT_METHOD_CALLED = "METHOD_CALLED"
EVENT_METHOD_SUCCEEDED = "METHOD_SUCCEEDED"
EVENT_METHOD_FAILED = "METHOD_FAILED"


class TelemetryEvent:
    def __init__(
        self,
        sk: str,
        event: str,
        payload: Optional[dict[str, Any]],
        sampling_rate: Optional[float] = 1.0,
    ):
        self.sk = sk
        self.event = event
        self.payload = payload
        self.it = "development" if sk and sk.startswith("sk_test") else "production"
        self.sampling_rate = sampling_rate
