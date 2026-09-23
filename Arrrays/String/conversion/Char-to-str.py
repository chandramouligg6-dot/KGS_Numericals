# Character string to integer conversion 

def chartoint(s):
    num = 0
    for i in s:
        if '0' <= i <= '9':
            num = (num * 10) + (ord(i) - 48)
    return num
    
s = input("Enter a string: ")
res = chartoint(s)
print("The Character string to integer result is: ", res)