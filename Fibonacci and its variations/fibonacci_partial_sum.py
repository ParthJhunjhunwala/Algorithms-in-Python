# Uses python3
# Result of sum repeats itself after every 300 iteration
def fibonacci_partial_sum(a, b):
    if b <= 1:
        return b
    else:
        a, b = a%300, b%300
        l = [0, 1]
        for i in range(2, 301):
            l.append((l[i-1] + l[i-2])%10)
        if a<=b:
            l = l[a:b+1]
        else:
            l = l[a:] + l[:b+1]
    return (sum(l) % 10)

if __name__ == '__main__':
    n = input()
    from_, to = map(int, n.split())
    print(fibonacci_partial_sum(from_, to))