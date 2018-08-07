#python3
'''
Introduction problem. This problems takes two integers and returns the sum

Input: 7 6
Returns: 13

This code was already provided to us by the instructors
'''


def sum_of_two_digits(a, b):
    return a + b


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_of_two_digits(a, b))
