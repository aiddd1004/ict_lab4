products = {
    "apple": 2,
    "banana": 1,
    "milk": 3,
    "bread": 2,
    "eggs": 4
}

total = 0

for item, price in products.items():
    print(item, ":", price)
    total += price

print("Total cost:", total)
