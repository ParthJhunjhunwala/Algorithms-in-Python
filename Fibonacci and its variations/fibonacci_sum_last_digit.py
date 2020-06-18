# Uses python3
# Result of sum repeats itself after every 300 iteration
def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    else:
        l = [0, 1]
        for i in range(2, n % 300 + 1):
            l.append((l[i-1] + l[i-2]) % 10)
    return (sum(l) % 10)

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_naive(n))