def stringWithSum(s):
    nstr = ""
    num = 0
    total = 0
    
    for i in range(len(s)):
        if '0' <= s[i] <= '9':
            num = num * 10 + (ord(s[i]) - 48)
        else:
            total += num
            num = 0
            nstr += s[i]
    
    total += num
    return nstr + str(total)

s = input("Enter a string along with integer values (eg: abc123): ")
res = stringWithSum(s)
print("The summed digit along with strings:", res)