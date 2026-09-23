# integer to string conversion 

def inttostring(num):
    nstr = ""
    while num > 0:
        rem = num % 10
        nstr = chr(rem + 48) + nstr
        num = num // 10
    return nstr

num = int(input("Enter a number: "))
res = inttostring(num)
print("The number to string result is: ", res)