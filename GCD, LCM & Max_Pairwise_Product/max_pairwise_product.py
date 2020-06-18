# python3
def max_pairwise_product(numbers):
    max_1 = numbers.index(max(numbers))
    max_2 = -1
    for i in range(len(numbers)):
        if (i != max_1) and ((max_2 == -1) or (numbers[i] > numbers[max_2])):
            max_2 = i
    return numbers[max_1]*numbers[max_2]

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))