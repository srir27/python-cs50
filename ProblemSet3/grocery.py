groceries = {}
while True:
    try:
        item = input().upper()
        if item not in groceries:
            groceries[item] = 1
        else:
            groceries[item] +=1
        continue

    except (KeyboardInterrupt, EOFError):
        break
for k in sorted(groceries):
    print(f"{groceries.get(k)} {k}")