# How to Use the Plagiarism Detection Code

1. **Using Text Directly:**

text = "your_text_here".replace('\n', '').replace('\t', '').split(',')
if detect_plagiarism(text):

2. **Using Text from a File:**

# Read text from a file
with open('your_file.txt', 'r') as file:
text = file.read().replace('\n', '').replace('\t', '').split(',')
if detect_plagiarism(text):


Remember to replace `'your_text_here'` with your actual text or provide the correct file path in `'your_file.txt'`.