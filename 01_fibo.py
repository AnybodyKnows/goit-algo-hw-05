import time as t

def caching_fibonacci():
    """Function with cashe"""
    cashe = {}

    def fibonacci(n):
        if n <=0: return 0
        elif n==1: return 1
        elif n in cashe:
            # print(f"easy work--{n}")
            return cashe[n]
        z = fibonacci(n-1) + fibonacci(n-2)
        cashe[n]=z
        # print(f"hard work--{n}")
        return z
    return fibonacci





fibo = caching_fibonacci()
print(fibo(10))
print(fibo(15))
