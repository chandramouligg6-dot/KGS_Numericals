# lower to upper case string conversion

def lowertoupper(s):
    l1 = list(s)
    for i in range(0, len(l1)):
        if 'a' <= l1[i] <= 'z':
            l1[i] = chr(ord(l1[i]) - 32)
    return "".join(l1)

s = input("Enter a String: ")
res = lowertoupper(s)
print("The original string is: ", s)
print("The lowercase uppercase string is : ", res)