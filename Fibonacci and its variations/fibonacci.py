# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    else:
        curr, new = 0, 1
        for i in range(2, n+1):
            curr, new = new, curr + new
    return new

n = int(input())
print(calc_fib(n))