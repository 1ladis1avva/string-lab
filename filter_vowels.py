text = input("Text: ")
vowels = "aeiouAEIOU"
filtered = "".join([c for c in text if c not in vowels])
print(filtered)
