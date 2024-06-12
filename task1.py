
# Find the number of words in the following text that start with a capital letter. Use the space as the word separator.
text = "If you need to Link to some research from a website or on social media, We want to encourage you to .Link to a RePEc page instead of directly to the full text."

words = text.split()
count = 0

for word in words:
    if word[0].isupper():
        count += 1

print(count)

