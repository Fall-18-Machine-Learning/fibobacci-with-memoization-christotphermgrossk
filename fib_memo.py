fibcache = {}

def fibmem(n):
    if n not in fibcache.keys():
        fibcache[n] = fib(n)
    return fibcache[n]

def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = fibmem(int(input("Enter an integer: ")))
print("The answer is: ", n)
