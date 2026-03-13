
data = {
    "name": "Alice",
    "age": 25
}


required_variables = ["name", "age", "email", "phone"]


missing = []

for var in required_variables:
    if var not in data:
        missing.append(var)


if missing:
    print("Missing variables:", missing)
else:
    print("No variables missing")

    print("total missing values : ")
