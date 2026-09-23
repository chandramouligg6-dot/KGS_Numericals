# WAP to sum the numbers(num is formed with continuous digits)in a given string

def sumNumbers(s):
    num = 0
    total = 0
    
    for i in range(len(s)):
        if '0' <= s[i] <= '9':
            num = num * 10 + (ord(s[i]) - 48)
        else:
            total += num
            num = 0
    
    total += num
    return total

s = input("Enter a string along with integer values (eg: abc123): ")
res = sumNumbers(s)
print("Sum of numbers:", res)