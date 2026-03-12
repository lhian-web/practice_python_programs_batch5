# Input full name
full_name = input("Enter your full name (incorrect casing): ")

# Split into words
words = full_name.split()
snake_case = ""

# Lowercase every word
for i in range(len(words)):
    word = words[i].lower()
    snake_case += word
    # Add underscore
    if i < len(words) - 1:
        snake_case += "_"

# print in snake casing
print(snake_case)