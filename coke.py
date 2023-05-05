def getCoinValue(coin):

    if coin == 25 or coin == 10 or coin == 5:
        return coin
    else:
        return 0
    
total = 0

while total < 50:
    coin = int(input("input a coin(25, 10 or 5): "))
    coin_value = getCoinValue(coin)
    if coin_value == 0:
       print("sorry!invalid coin.")
       continue
    total += coin_value
    print(f"Amount due:{50 - total} cents.")

change = total - 50
print(f"change owed: {change} cents.")
 
    