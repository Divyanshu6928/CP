def num(s,n):
    if(s<=n):
        print(s)
    else:
        return
    num(s+1,n)

s=1
n=int(input())
print("Numbers from 1 to",n,"are : ")
num(s,n)