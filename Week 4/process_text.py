# Step 1: Read contents from input.txt
with open('input.txt', 'r') as file:
    content = file.read()

# Step 2: Count the number of words
word_count = len(content.split())

# Step 3: Convert text to uppercase
uppercase_content = content.upper()

# Step 4: Write the processed text and word count to output.txt
with open('output.txt', 'w') as file:
    file.write("Processed Text (in Uppercase):\n")
    file.write(uppercase_content + "\n")
    file.write(f"\nTotal Word Count: {word_count}\n")

# Step 5: Print success message
print("✅ Success! 'output.txt' has been created with the processed content.")
