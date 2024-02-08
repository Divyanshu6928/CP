def calculate(a,b,m):
    cal=(a**b)%m
    return cal

a=int(input())
b=int(input())
m=int(input())
print(calculate(a,b,m))
