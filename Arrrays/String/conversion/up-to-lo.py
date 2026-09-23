# upper to lower case string conversion

def uppertolower(s):
    l1 = list(s)
    for i in range(0, len(l1)):
        if 'A' <= l1[i] <= 'Z':
            l1[i] = chr(ord(l1[i]) + 32)
    # join is the shortcut for concatenation
    return "".join(l1)

s = input("Enter a String: ")
res = uppertolower(s)
print("The original string is: ", s)
print("The uppercase to lowercase string is : ", res)