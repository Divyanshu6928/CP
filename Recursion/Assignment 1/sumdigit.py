def sumdigit(a):
    sum=0
    for i in range(len(a)):
        sum=sum+a[i]
    return sum

n=list(map(int,input().split()))
print(sumdigit(n))