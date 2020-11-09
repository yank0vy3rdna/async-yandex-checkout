import uuid
from enum import Enum

from async_yandex_checkout.connector import Connector


class Status(Enum):
    PENDING = 'pending'
    WAITING_FOR_CAPTURE = 'waiting_for_capture'
    SUCCEEDED = 'succeeded'
    CANCELED = 'canceled'


class Payment:
    base_path = 'payments'
    client = None
    idempotency_key = None
    id = None
    status = None
    paid = None
    confirmation_url = None
    payment_object = None

    def __init__(self):
        self.client = Connector()

    async def create(self, amount: int, description: str, return_url: str, idempotency_key=None):
        if self.idempotency_key is None:
            if idempotency_key is None:
                idempotency_key = str(uuid.uuid4())
            self.idempotency_key = idempotency_key
        else:
            idempotency_key = self.idempotency_key
        data = {
            "amount": {
                "value": f"{int(amount)}.00",
                "currency": "RUB"
            },
            "capture": True,
            "confirmation": {
                "type": "redirect",
                "return_url": return_url
            },
            "description": description
        }
        response = await self.client.request(self.base_path, data, {"Idempotence-Key": idempotency_key})
        self.update_fields(response)

    def update_fields(self, response):
        self.status = Status(response.get("status"))
        self.id = response.get("id")
        self.confirmation_url = response.get("confirmation").get("confirmation_url")
        self.payment_object = response

    async def update(self, payment_id=None, idempotency_key=None):
        if payment_id is None:
            payment_id = self.id
        if self.idempotency_key is None:
            if idempotency_key is None:
                idempotency_key = str(uuid.uuid4())
            self.idempotency_key = idempotency_key
        else:
            idempotency_key = self.idempotency_key

        response = await self.client.request(f"{self.base_path}/{payment_id}",
                                             headers={"Idempotence-Key": idempotency_key}, method='GET')
        self.update_fields(response)
