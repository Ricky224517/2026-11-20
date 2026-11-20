def fun1(n):          #費式數列
    if n == 0 or n == 1:
        return n
    else:
        return fun1(n-2) + fun1(n - 1)
n = int(input())  
print(fun1(n))