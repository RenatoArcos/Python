# pip install forex-python
from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = float(input("Enter the amount:  "))
from_currency = input("From Currency:  ").upper()
to_currency = input("To Currency:  ").upper()

print("\n", amount, from_currency, "To", to_currency)
result = c.convert(from_currency, to_currency, amount)
print(result, "\n")

#by clcoding.com
