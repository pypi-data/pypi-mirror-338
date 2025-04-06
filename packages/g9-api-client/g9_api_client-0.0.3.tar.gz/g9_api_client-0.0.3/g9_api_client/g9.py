import aiohttp
import logging
from .constants import LOGIN_URL, INVOICES_URL, CONTRACTS_URL, ELECTRICITY_CONSUMPTION_URL, GAS_CONSUMPTION_URL

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.DEBUG)


class G9:
    def __init__(self, session: aiohttp.ClientSession, username, password):
        self.token = None
        self._username = username
        self._password = password
        self._session = session

    async def __api_request(self, url: str, method="get", data=None, params=None, headers=None):
        async with getattr(self._session, method)(url, headers=headers or self._get_headers(), json=data,
                                                  params=params, ssl=False) as response:
            try:
                if response.status == 200 and response.content_type == 'application/json':
                    json_response = await response.json()
                    return json_response
                else:
                    raise Exception(f"HTTP Request Error: %s", str(response.status) + " " + str(response.content_type))
            except Exception as err:
                _LOGGER.error(f"API request error: %s", err)
                return None

    async def login(self):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': self._username,
            'password': self._password
        }
        print("Logging in...", LOGIN_URL)
        print("Logging in with username:", self._username)

        result = await self.__api_request(LOGIN_URL, method="post", data=data, headers=headers)
        data = result.get('data')
        if data:
            self.token = data.get('token')
            if self.token:
                return True
        return False

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.token}",
            "Cookie": f"BEARER={self.token}"
        }

    async def get_contracts(self):
        if not self.token:
            _LOGGER.error("Not logged in - token not found")
            raise Exception("Not logged in")
        result = await self.__api_request(CONTRACTS_URL)
        contracts = result.get('contracts')
        if contracts:
            return contracts
        return None

    async def get_last_invoice(self, contract_id):
        if not self.token:
            _LOGGER.error("Not logged in - token not found")
            raise Exception("Not logged in")
        params = {
            "contractId": contract_id
        }
        result = await self.__api_request(INVOICES_URL, params=params)
        invoice = result.get('invoice')
        if invoice:
            return invoice
        return None

    async def get_last_electricity_consumption(self, contract_id):
        if not self.token:
            _LOGGER.error("Not logged in - token not found")
            raise Exception("Not logged in")
        params = {
            "contractId": contract_id
        }
        result = await self.__api_request(ELECTRICITY_CONSUMPTION_URL, params=params)
        electricity = result.get('electricity_graph')
        if electricity:
            return electricity
        return None

    async def get_last_gas_consumption(self, contract_id):
        if not self.token:
            _LOGGER.error("Not logged in - token not found")
            raise Exception("Not logged in")
        params = {
            "contractId": contract_id
        }
        result = await self.__api_request(GAS_CONSUMPTION_URL, params=params)
        gas = result.get('gas_graph')
        if gas:
            return gas
        return None
