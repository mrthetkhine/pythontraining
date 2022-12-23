vowels = ['a','e','i','o','u']
input_str = input("Enter input: ")
vowel_list = []

for vowel in vowels:
    if vowel in input_str:
        vowel_list.append(vowel)
print("Vowel list ",vowel_list)

another = [vowel for vowel in vowels if vowel in input_str]
print("Another vowel list ",another)