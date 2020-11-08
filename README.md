![Upload Python Package](https://github.com/yank0vy3rdna/async-yandex-checkout/workflows/Upload%20Python%20Package/badge.svg)
# async_yandex_checkout

Async yandex checkout api wrapper for python

## Example of usage

```python
from async_yandex_checkout.configuration import configuration
from async_yandex_checkout.payment import Payment
import asyncio

configuration.configure("shop_id", "secret_key")
loop = asyncio.get_event_loop()
payment = Payment()
loop.run_until_complete(
    payment.create(1000000, "description", "redirect_url")
)

loop.run_until_complete(
    payment.update()
)
print(payment.status)
```