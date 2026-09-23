# Reversing the string using recursion.

def reversestring1(s,nstr,i):
    if i < 0:
        return nstr
    nstr += s[i]
    return reversestring1(s,nstr,i - 1)

s = input("Enter a string that you wish to reverse: ")
res = reversestring1(s,"",len(s)-1)
print("The Reversed string is:",res)