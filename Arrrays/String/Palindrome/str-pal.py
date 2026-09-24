# WAP to check whether the given string is a palindrome or not

def filterations(s):
    nstr =""
    for i in s:
        if "A" <= i <= "Z":
            nstr += chr(ord(i) + 32)
        elif "0" <= i <= "9" or "a" <= i <= "z":
            nstr += i
    return nstr 

def isStringPalindrome(s):
    s = filterations(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

s = input("Enter a string to check whether it is a palindrome or not: ")
flag = isStringPalindrome(s)
if flag:
    print("The given string is a Palindrome")
else:
    print("The given string is not a Palindrome")

    