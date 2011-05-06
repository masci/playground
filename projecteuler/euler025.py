"""What is the first term in the Fibonacci sequence to contain 1000 digits?
"""
memo = {0:0, 1:1}

def fib(n, memo):
    if not n in memo:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

if __name__ == "__main__":
    n = 0
    f = str(0)
    while len(f) < 1000:
        n += 1
        f = str(fib(n, memo))
        
print n,f