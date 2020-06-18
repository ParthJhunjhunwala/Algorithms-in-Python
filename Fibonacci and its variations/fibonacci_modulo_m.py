# Uses python3
# for any integer m >= 2, seq Fn mod m is periodic and period always
# starts with 01. We store the (n mod m) values in a list until we 
# encounter 01. We remove the 01 and now have the recurring values in a list.
def get_fibonacci_huge_naive(n, m):
    l = [0, 1]
    for i in range(2, n+1):
        l.append((l[i-1] + l[i-2])%m)
        if l[i] == 1 and l[i-1] == 0:
            l = l[:-2]
            break
    return l[n % len(l)]

if __name__ == '__main__':
    num = input()
    n, m = map(int, num.split())
    print(get_fibonacci_huge_naive(n, m))