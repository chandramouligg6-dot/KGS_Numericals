# sum of the digits in a string 

def sumDigit(s):
    nstr = ""
    num = 0
    for i in range(0, len(s)):
        if '0' <= s[i] <= '9':
            num = num + (ord(s[i]) - 48)
        else:
            nstr += s[i]
    return nstr + str(num)
    
s = input("Enter a string along with integer values (eg: abc123): ")
res = sumDigit(s)
print("The sumed digit along with stings: ", res)