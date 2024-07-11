<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from clerk_backend_api import Clerk
import os

s = Clerk(
    bearer_auth=os.getenv("BEARER_AUTH", ""),
)


res = s.email_addresses.get(email_address_id="email_address_id_example")

if res is not None:
    # handle response
    pass
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from clerk_backend_api import Clerk
import os

async def main():
    s = Clerk(
        bearer_auth=os.getenv("BEARER_AUTH", ""),
    )
    res = await s.email_addresses.get_async(email_address_id="email_address_id_example")
    if res is not None:
        # handle response
        pass

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->