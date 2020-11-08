import aiohttp

from async_yandex_checkout.configuration import configuration


class Connector:
    base_url = 'https://payment.yandex.net/api/v3/'

    async def request(self, url, data=None, headers=None, method='POST'):
        if headers is None:
            headers = {}
        auth = aiohttp.BasicAuth(login=configuration.shop_id, password=configuration.secret_key, encoding='utf-8')
        async with aiohttp.ClientSession(auth=auth) as session:
            async with session.request(method, self.base_url + url, headers=headers, json=data) as response:
                return await response.json()
