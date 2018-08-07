#python3
'''
Introduction problem.

Input format: The first line contains an integer n. The next line contains n non-negative integers
a1; : : : ;an (separated by spaces).

Output format: The maximum pairwise product.

Constraints. 2 <= n <= 2^(10^5); 0 <= a1; : : : ;an <= 2^(10^5).

Input:
3
1 2 3
Returns: 6

The naive solution was provided to us by instructors. It is not fast enough to meet the time deadline of 5 seconds
'''


def naive_max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])

    return max_product


def faster_max_pairwise_product(numbers):
    max_number = None
    max_number2 = None
    max_index = None

    for ind, val in enumerate(numbers):
        if not max_number or val > max_number:
            max_index = ind
            max_number = val

    for ind, val in enumerate(numbers):
        if (not max_number2 or val > max_number2) and ind != max_index:
            max_number2 = val

    return max_number * max_number2


if __name__ == '__main__':
    input_n = input()
    input_numbers = [int(x) for x in input().split()]
    print(faster_max_pairwise_product(input_numbers))