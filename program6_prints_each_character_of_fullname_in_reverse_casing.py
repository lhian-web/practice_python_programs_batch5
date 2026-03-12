# Input full name
full_name = input("Enter your full name (incorrect casing): ")
reverse_case = ""

# Reverse casing
for char in full_name:
    if char.islower():
        reverse_case += char.upper()
    elif char.isupper():
        reverse_case += char.lower()
    else:
        reverse_case += char

# Print name in reverse casing
print(reverse_case)