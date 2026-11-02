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

print(customer.get("ytd_spend", "0"))

print("--- Exercise 3 ---")
print(customer.get("email", "no email on file"))

# try:
#     print(customer["email"])
# except KeyError as error:
#     print("KeyError caught: ", error)

print("--- Exercise 4 ---")

for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)

print("--- Exercise 5 ---")
tier_discounts = {
    "bronze":0,
    "silver": 0.05, 
    "gold": 0.1, 
    "platinum": 0.15}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: {final_price:.2f}")



   