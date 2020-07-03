customer = {
    "name": "Vishal Khandekar",
    "age": 31,
    "is_verified": True
}
print(customer["name"])
print(customer.get("birthdate"))
print(customer.get("birthdate", "Jan 1 1980"))
'''It will get default value'''

customer["name"]= "Milind Thorat"
print(customer.get("name"))

customer["address"] = "Kurla"
print(customer.get("address"))
