amount_due = 50
accepted = [5, 10, 25]
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in accepted:
        amount_due = amount_due - insert_coin
        # print(f"Change Owed: {amount_due}")
if amount_due < 0:
    print(f"Change Owed: { - amount_due}")
else:
    print("Change Owed: 0")
