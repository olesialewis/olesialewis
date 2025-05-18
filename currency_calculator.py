#currency  convertion
# convert dollar to zloty
# url  https://v6.exchangerate-api.com/v6/4d504e76133a400bf7ece30c/pair/USD/PLN
import requests

def dollar_to_zloty(dollar):
    url = "https://v6.exchangerate-api.com/v6/4d504e76133a400bf7ece30c/pair/USD/PLN"
    response = requests.get(url)

    zloty_rate = response.json()["conversion_rate"]
    return round(dollar * zloty_rate, 2)
  
amount =int(input("Enter the amount in dollars: "))
print(f"Converted amount is : {dollar_to_zloty(amount)} zloty")                                                                     