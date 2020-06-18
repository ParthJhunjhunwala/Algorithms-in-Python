# Uses python3
# Logic: a * b = gcd(a, b) * lcm(a, b)
def gcd_for_lcm(a, b):
    while True:
        if (b == 0):
            return a
        else:
            a, b = b, a%b

if __name__ == '__main__':
    num = input()
    a, b = map(int, num.split())
    gcd_cal = gcd_for_lcm(a, b)
    print(int(a * b / gcd_cal))
