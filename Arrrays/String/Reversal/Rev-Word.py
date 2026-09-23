# Reversal of words in a string 

def reverse_words(s):
    s = s + " " # Add extra space for extra cycle to reverse the last word 
    nsen = ""
    nword = ""
    for i in range(0, len(s)):
        if s[i] != " ":
            nword = s[i] + nword
        elif nword != "":
            if nsen == "":
                nsen = nsen + nword
            else:
                nsen = nsen + " " + nword
            nword = ""
    return nsen

s = input("Enter a string that you wish to reverse the words: ")
res = reverse_words(s)
print("The Reversed words string is:", res)