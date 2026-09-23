# reverse a string 

# Reversal of string logic 1 that is incrementing loop

def reversesrting2(s):
    nstr = ""
    for i in range(0, len(s)):
        nstr = s[i] + nstr
    return nstr 

s = input("Enter a string that you wish to reverse: ")
print("Original String is: ",s)
res = reversesrting2(s)
print("The Reversed string is:",res)