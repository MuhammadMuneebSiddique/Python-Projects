import requests

from_currency = input("Enter the Currency: ").upper()
to_currency = input(f"Enter the currency from convert {from_currency}: ").upper()
amount = int(input(f"Enter the amount of {from_currency} to convert {to_currency}: "))

api = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
response = requests.get(api)
rate = response.json()

result = rate["rates"][to_currency] * amount
print(f"Today One {from_currency} Rates in {to_currency}: {rate["rates"][to_currency]}")
print(f"{amount} {from_currency} in {to_currency}: {result}")
