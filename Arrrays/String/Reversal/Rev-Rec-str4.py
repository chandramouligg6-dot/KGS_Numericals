# Reversing the string using recursion with using incrementing.

def reversestring1(s,nstr,i):
    if i == len(s):
        return nstr
    nstr = s[i] + nstr
    return reversestring1(s,nstr,i + 1)

s = input("Enter a string that you wish to reverse: ")
res = reversestring1(s,"",0)
print("The Reversed string is:",res)