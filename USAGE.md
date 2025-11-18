<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from clerk_backend_api import Clerk


with Clerk(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as clerk:

    res = clerk.email_addresses.get(email_address_id="email_address_id_example")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
from clerk_backend_api import Clerk

async def main():

    async with Clerk(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as clerk:

        res = await clerk.email_addresses.get_async(email_address_id="email_address_id_example")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->