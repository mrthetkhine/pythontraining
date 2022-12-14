str1 = 'kyaw Gyi'
first_char = ord(str1[0])-32
print("First Char ",chr(first_char))

words = str1.split()
print("Words ",words)
result = []
for word in words:
    first_char = ord(word[0])
    if(chr(first_char).isupper()):
        upperChar =chr(first_char - 32)
        #print("First Char is lowercase ",word[0], "Uppercaes ",upperChar)
        reaming_char = word[1:]
        #print("reaming_char",reaming_char)
        trasformed_word = upperChar + reaming_char
        #print("trasformed_word",trasformed_word)
        result.append(trasformed_word)
    else:
        result.append(word)
result_str = " ".join(result)
print("Result ",result_str)