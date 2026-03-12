# Input full name
full_name = input("Enter your full name (incorrect casing): ")

# Split into words
words = full_name.split()
pascal = ""

# Capitalize every first letter of each word and combine
for word in words:
    pascal += word.capitalize()

# Print
print(pascal)