

def caching_fibonacci(n):
    cashe = {}

    def fibo(n):
        if n <=0:
            return 0
        elif n==1:
            return 1
        elif n in cashe:
            print("easy work")
            return cashe[n]
        
        f1 = fibo(n-1)
        f2 = fibo(n-2)
        z = f1+ f2
        cashe[n]=z
        print("hard work")
        return z
    return fibo(n)

        
         
    




a = caching_fibonacci(10)
print(a)
