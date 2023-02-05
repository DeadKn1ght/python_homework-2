# Задача 10: На столе лежат n монеток. Некоторые из них
# лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх
# одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть
#
# 5 -> 1 0 1 1 0
# 2

coins = int(input("Input how many coins are on the table :"))
print(f'Input side of the coin,where "0" - are heads and "1" are tails :')
coinsTails = 0
coinsHeads = 0
for count in range(coins) :
    coin = int(input())
    if coin == 0 :
        coinsHeads += 1
        # print(coinsHeads)
    elif coin == 1:
        coinsTails += 1
        # print(coinsTails)
    else :
        print("You input incorrect number")
    count += 1
# print(f"coinsTails = {coinsTails}")
# print(f"coinsHeads = {coinsHeads}")
if coinsTails > coinsHeads :
    turnCoins = coins - coinsTails
    print(f"You need to turn {turnCoins} Head sides of coins coins")
elif coinsHeads > coinsTails :
    turnCoins = coins - coinsHeads
    print(f"You need to turn {turnCoins} Tail sides of coins")
elif coinsHeads == coinsTails :
    print(f"No mather what side of coins to turn over.You need to turn {coinsHeads} coins")
