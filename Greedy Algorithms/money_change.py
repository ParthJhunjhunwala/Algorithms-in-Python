# Uses python3
def get_change(m):
    l = [10, 5 ,1]
    count = 0
    for i in l:
        count = count + m // i
        m = m - (i*(m // i))
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))