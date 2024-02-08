#MADAM       MADAM

def pali(s1):
    # for i in range(len(s)):
    s2=s1[::-1]
    if(s1==s2):
        print("Palindrome")
    else:
        print("Not a Palindrome")
s1=input()
pali(s1)