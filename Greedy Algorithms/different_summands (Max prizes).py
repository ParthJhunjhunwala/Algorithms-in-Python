# Uses python3
'''
8 => 1 2 5
16 => 1 2 3 4 6
This means the solution is always a sequence of integers and only the last element
is a different number.
The code explains the logic of finding the length of the seq and the last element
for the solution.
We decrease n by i as long as 2^i is less than n.

Time complexity: sqrt(n)
'''
def optimal_summands(n):
    if n == 1:
        return [1]
    for i in range(1, n):
        if 2 * i < n:
            n -= i
        else: break
    summands = [x for x in range(1, i)]
    summands.append(n)
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
