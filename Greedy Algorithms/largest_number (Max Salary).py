#Uses python3
'''
Take largest in every iteration, remove from list and append to result
largest between 4 and 435 will be 4.
This is because 4435 is greate than 4354.
'''
def isLarger(element, curr_max):
    if curr_max + element > element + curr_max:
        return False
    else:
        return True

def largest_number(a):
    res = ""
    while a != []:
        curr_max = a[0]
        for i in a:
            if isLarger(i, curr_max):
                curr_max = i
        res += curr_max
        a.remove(curr_max)
    return res

if __name__ == '__main__':
    n = input()
    a = input().split()
    print(largest_number(a))