# reverse a string 

# Reversal of string logic 1 that is decrementing loop
def reversestring1(s):
    nstr = ""
    for i in range(len(s) - 1, -1, -1):
        nstr += s[i]
    return nstr

s = input("Enter a string that you wish to reverse: ")
res = reversestring1(s)
print("The Reversed string is:",res)