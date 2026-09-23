# upper to lower and lower to upper string conversion

def switchchar(s):
    l1 = list(s)
    for i in range(0, len(l1)):
        if 'A' <= l1[i] <= 'Z':
            l1[i] = chr(ord(l1[i]) + 32)
        elif 'a' <= l1[i] <= 'z':
            l1[i] = chr(ord(l1[i]) - 32)
    return "".join(l1)

s = input("Enter a string: ")
res = switchchar(s)
print("The switched Character string is: ", res)