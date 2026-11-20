def fun1(n):          #遞迴數列
    if n == 2:
        return n
    else:
        return n * fun1(n - 1)
n = int(input())  
print(fun1(n))  