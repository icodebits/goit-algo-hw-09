def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    coin_count = {}
    for coin in coins:
        if amount >= coin:
            coin_count[coin] = amount // coin
            amount %= coin
    return coin_count

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_used = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                if min_coins[i - coins[j]] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coins[j]] + 1
                    coin_used[i] = j
                    
    coin_count = {}
    while amount > 0:
        coin_count[coins[coin_used[amount]]] = coin_count.get(coins[coin_used[amount]], 0) + 1
        amount -= coins[coin_used[amount]]
    
    return coin_count

if __name__ == "__main__":
    amount = 113
    print("Жадібний алгоритм:", find_coins_greedy(amount))
    print("Алгоритм динамічного програмування:", find_min_coins(amount))
