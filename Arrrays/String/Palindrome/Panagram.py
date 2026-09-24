# WAP to check whether the given string is a pangram or not.

def filterations(s):
    nstr =""
    for i in s:
        if "A" <= i <= "Z":
            nstr += chr(ord(i) + 32)
        elif "a" <= i <= "z":
            nstr += i
    return nstr 

def isPangram(s):
    s = filterations(s)
    if len(s) < 26:
        return False
    else:
        dict = {}
        for i in range(0, len(s)):
            if s[i] in dict:
                dict[s[i]] += 1
            else:
                dict[s[i]] = 1
    return len(dict) == 26

s = input("Enter a string to check whether it is a pangram or not: ")
flag = isPangram(s)
if flag:
    print("The given string is a Pangram")
else:
    print("The given string is not a Pangram")