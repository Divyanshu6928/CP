def duplicate(s):
    for i in range(len(s)-1):
            if(s[i]==s[i+1]):
                print(s[i])
                i+=1
            else:
                 break
            
s=input()
print(duplicate(s))

