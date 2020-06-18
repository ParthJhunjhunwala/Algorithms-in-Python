# Uses python3
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    else:
        curr, new = 0, 1
        for i in range(2, n+1):
            curr, new = new % 10, (curr + new) % 10
    return new

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
