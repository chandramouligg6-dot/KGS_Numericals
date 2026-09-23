# reversal string by converting into array

def reversal5(s):
    arr = list(s)
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return "".join(arr)


s = input("Enter a string that you wish to reverse: ")
res = reversal5(s)
print("The Reversed string is:", res)