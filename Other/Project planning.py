rows = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol: ")
for x in range(rows):
    for y in range(col):
        print(symbol, end = "")
    print()
