# customers.py
# Author: Ashley
# Module 11 Lab: Customer Dictionary & Lookup

print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])



print("--- Exercise 2 ---")
customer['phone'] = '555-5555' # adding a new key value to dictionary
print(customer)
customer['tier'] = 'platinum'
print(customer)
del customer['name']
print(customer)