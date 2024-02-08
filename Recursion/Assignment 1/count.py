def count(a,b):
    count=0
    if(a in b):
        for i in range(len(b)):
            if(b[i]==a):
                count+=1
    return count
a=int(input())
b=list(map(int,input().split()))
print(count(a,b))