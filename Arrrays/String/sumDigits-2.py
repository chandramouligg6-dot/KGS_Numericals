# Sum of digits in a string with only number output

def sumDigit(s):
    nstr = ""
    num = 0
    for i in range(0, len(s)):
        if '0' <= s[i] <= '9':
            num = num + (ord(s[i]) - 48)
        else:
            nstr += s[i]
    return num

s = input("Enter a string along with integer values (eg: abc123): ")
res = sumDigit(s)
print("The sum up of character digits is: ", res)