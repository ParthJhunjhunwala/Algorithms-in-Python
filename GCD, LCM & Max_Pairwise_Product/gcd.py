# Uses python3
def gcd(a, b):
    while True:
        if (b == 0):
            return a
        else:
            a, b = b, a % b

if __name__ == "__main__":
    num = input()
    a, b = map(int, num.split())
    print(gcd(a, b))
