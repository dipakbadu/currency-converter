# app/services/currency_converter.py
import os
import httpx
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

API_KEY = os.getenv("EXCHANGE_API_KEY")
API_URL = "https://v6.exchangerate-api.com/v6"

class CurrencyConverter:
    def __init__(self):
        if not API_KEY:
            raise ValueError("API Key is missing! Please set EXCHANGE_API_KEY in .env")
        self.api_key = API_KEY
        self.api_url = API_URL

    async def convert(self, from_currency: str, to_currency: str, amount: float) -> dict:
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        url = f"{self.api_url}/{self.api_key}/latest/{from_currency}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        if response.status_code != 200:
            raise Exception("API request failed with status code " + str(response.status_code))

        data = response.json()

        if data.get("result") != "success":
            raise Exception("API error: " + data.get("error-type", "Unknown error"))

        rates = data.get("conversion_rates")
        if not rates or to_currency not in rates:
            raise Exception(f"Invalid target currency code: {to_currency}")

        rate = rates[to_currency]
        converted_amount = round(amount * rate, 4)

        return {
            "from": from_currency,
            "to": to_currency,
            "original_amount": amount,
            "converted_amount": converted_amount,
            "rate": rate
        }

    async def get_supported_currencies(self):
        async with httpx.AsyncClient() as client:
            url = f"{self.api_url}/{self.api_key}/codes"
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            codes = data.get("supported_codes", [])
            return [{"code": code, "currency": name} for code, name in codes]
