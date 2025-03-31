<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from clerk_backend_api import Clerk


with Clerk() as clerk:

    clerk.miscellaneous.get_public_interstitial(frontend_api_query_parameter="frontend-api_1a2b3c4d", frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="pub_1a2b3c4d", proxy_url="https://mean-orchid.com/", domain="plump-reach.com", sign_in_url="https://delicious-costume.org/", use_domain_for_script=True)

    # Use the SDK ...
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from clerk_backend_api import Clerk

async def main():

    async with Clerk() as clerk:

        await clerk.miscellaneous.get_public_interstitial_async(frontend_api_query_parameter="frontend-api_1a2b3c4d", frontend_api_query_parameter1="pub_1a2b3c4d", publishable_key="pub_1a2b3c4d", proxy_url="https://mean-orchid.com/", domain="plump-reach.com", sign_in_url="https://delicious-costume.org/", use_domain_for_script=True)

        # Use the SDK ...

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->