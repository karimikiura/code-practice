'''
Author: nkarimi@linux.com
Approach: incremental development - debugging by adding and testing only a small amount of code at a time.
'''

def factorial(n):
    # base case
    if not isinstance(n, int):
        print("The fatorial is only defined for integers.")
        return -1
    elif n < 0:
        print("The fatorial is only defined for positive integers.")
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

prompt = 'Which number would you like to calculate a factorial for?\n'

print(prompt)
number = int(input())
res = factorial(number)
print(f"The FACTORIAL for {number}! is: {res}")
