import time as t

def caching_fibonacci(n):
    """Function with cashe"""
    cashe = {}

    def fibo(n):
        if n <=0:
            return 0
        elif n==1:
            return 1
        elif n in cashe:
            # print(f"easy work--{n}")
            return cashe[n]
        z = fibo(n-1) + fibo(n-2)
        cashe[n]=z
        # print(f"hard work--{n}")
        return z
    return fibo(n)

def fibonacci(n):
    """Function WITHOUT cashe"""
    def fibo(n):
        if n <=0:
            return 0
        elif n==1:
            return 1
        z = fibo(n-1) + fibo(n-2)
        return z
    return fibo(n)


itter = 35
nach = t.time()
a = caching_fibonacci(itter)
print(a)
print(f"time of running {itter} times with cashe {float(t.time()-nach)}")


nach1 = t.time()
a = fibonacci(itter)
print(a)
print(f"time of running {itter} times WITHOUT cashe  {float(t.time()-nach1)}")