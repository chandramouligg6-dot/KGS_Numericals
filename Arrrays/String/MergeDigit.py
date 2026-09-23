# merge all the digits in a string 
# Enter a string:  Le44wis44cl16
# The Character string to integer result is:  444416

def sumDigit2(s):
    num = 0
    for i in range(0, len(s)):
        if '0' <= s[i] <= '9':
            num = (num * 10) + (ord(s[i]) - 48)
    return num
    
s = input("Enter a string: ")
res = sumDigit2(s)
print("The Character string to integer result is: ", res)