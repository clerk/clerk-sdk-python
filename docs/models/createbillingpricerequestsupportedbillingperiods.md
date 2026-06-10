# CreateBillingPriceRequestSupportedBillingPeriods

Which billing periods this price supports. Inferred from amounts if omitted.

## Example Usage

```python
from clerk_backend_api.models import CreateBillingPriceRequestSupportedBillingPeriods

value = CreateBillingPriceRequestSupportedBillingPeriods.MONTH
```


## Values

| Name     | Value    |
| -------- | -------- |
| `MONTH`  | month    |
| `ANNUAL` | annual   |
| `BOTH`   | both     |