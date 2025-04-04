import httpx

from .constants import LOGIN_URL, INVOICES_URL, CONTRACTS_URL, ELECTRICITY_CONSUMPTION_URL, GAS_CONSUMPTION_URL


class G9:
    def __init__(self, username, password):
        self.token = None
        self.username = username
        self.password = password

    def login(self):
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'username': self.username,
            'password': self.password
        }
        print("Logging in...", LOGIN_URL)
        print("Logging in with username:", self.username)
        response = httpx.post(LOGIN_URL, json=data, headers=headers)
        if response.status_code == 200:
            result = response.json()
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

    def get_contracts(self):
        response = httpx.get(CONTRACTS_URL, headers=self._get_headers())
        if response.status_code == 200:
            result = response.json()
            contracts = result.get('contracts')
            if contracts:
                return contracts
        return None

    def get_last_invoice(self, contract_id):
        if self.token:
            params = {
                "contractId": contract_id
            }
            response = httpx.get(INVOICES_URL, params=params, headers=self._get_headers())
            if response.status_code == 200:
                result = response.json()
                invoice = result.get('invoice')
                if invoice:
                    return invoice
        return None

    def get_last_electricity_consumption(self, contract_id):
        params = {
            "contractId": contract_id
        }
        response = httpx.get(ELECTRICITY_CONSUMPTION_URL, params=params, headers=self._get_headers())
        if response.status_code == 200:
            result = response.json()
            electricity = result.get('electricity_graph')
            if electricity:
                return electricity
        return None

    def get_last_gas_consumption(self, contract_id):
        params = {
            "contractId": contract_id
        }
        response = httpx.get(GAS_CONSUMPTION_URL, params=params, headers=self._get_headers())
        if response.status_code == 200:
            result = response.json()
            gas = result.get('gas_graph')
            if gas:
                return gas
        return None
