def solution(p, n):
    save_value = {}

    def find_max_profit(p, n):
        if n == 0:
            return 0
        maximum_price = -1
        for i in range(1, n+1):
            if n - i in save_value:
                last_profit = save_value[n - i]
            else:
                last_profit = find_max_profit(p, n-i)
                save_value[n - i] = last_profit
            maximum_price = max(maximum_price, p[i] + last_profit)
        return maximum_price
    return find_max_profit(p, n)

p = [0, 1, 5, 8, 9]
n = 4

print(solution(p, n))