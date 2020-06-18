# Result of sum of squares repeats itself after every 30 iteration
# sum of sq till F(i) = F(i) * (F(i) + F(i-1))
# sum of sq for F(5) = 0 + 1 + 1 + 4 + 9 = 15
# F(5) * (F(4) + f(5)) = 3 * (2+3) = 15
def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    else:
        l = [0, 1]
        for _ in range(2, n+1):
            l = [l[1], l[0] + l[1]]
    return (l[1] * (l[0] + l[1]))%10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n % 30))