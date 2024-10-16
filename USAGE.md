<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from clerk_backend_api import Clerk

s = Clerk()


s.miscellaneous.get_public_interstitial(frontend_api="frontend-api_1a2b3c4d", publishable_key="pub_1a2b3c4d")

# Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from clerk_backend_api import Clerk

async def main():
    s = Clerk()
    await s.miscellaneous.get_public_interstitial_async(frontend_api="frontend-api_1a2b3c4d", publishable_key="pub_1a2b3c4d")
    # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->