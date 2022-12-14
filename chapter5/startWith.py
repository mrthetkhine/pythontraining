str1 = "Hello December"
print("startWith Hello ", str1.startswith('Hello'))
print("endWith December ", str1.endswith('December'))

special_chars = '!~@#$%^@(*'
special_chars_list = list(special_chars)
print("Special ",special_chars_list)
print("isalpha aeze122 ", 'aeze122'.isalnum())
print("isdigit 12 ", '12'.isdigit())
print("isdigit 12A ", '12A'.isdigit())
print("isupper A ", 'A'.isupper())
print("! is speical char ", '2' in special_chars_list)