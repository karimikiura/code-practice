'''
Author: nkarimi@linux.com
fibonacci(0) = 1
fibonacci(1) = 1
fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2);
'''

def fibonnaci(n):
    # base case 
    if n == 0 or n == 1:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n -2)

print(fibonnaci(12))