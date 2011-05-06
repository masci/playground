"""
Given the first few numbers of the Fibonacci sequence:

1 1 2 3 5 8 13 21 ...

What is the first Fibonacci number to contain 15 digits?
"""
def fiborange(limit):
    n, f = 0, 1
    while (f <= limit):
        yield f
        n, f = f, f+n

def main():
    for x in fiborange(10**20):
        if len(str(x)) == 15:
            print x
            break

if __name__ == "__main__":
    main()
