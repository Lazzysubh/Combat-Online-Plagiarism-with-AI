import nltk

# Download the Gutenberg corpus
nltk.download('gutenberg')

# Load the dataset of online content
dataset = nltk.corpus.gutenberg.words('austen-emma.txt')

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Preprocess the text data
stop_words = set(stopwords.words('english'))
dataset = [word.lower() for word in dataset if word not in stop_words]

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(dataset)

# Function to detect plagiarism
def detect_plagiarism(text):
    # Preprocess the text
    text = [word.lower() for word in text if word not in stop_words]

    # Create a TF-IDF vector for the input text
    tfidf_text = vectorizer.transform(text)

    # Calculate cosine similarity between the input text and the dataset
    similarity = cosine_similarity(tfidf_text, tfidf_matrix)[0]

    # Determine if plagiarism is detected
    if any(similarity > threshold):
        return True
    else:
        return False

# Set the plagiarism threshold
threshold = 0.8

# Read text from a file
with open('your_file.txt', 'r') as file:
    text = file.read().replace('\n', '').replace('\t', '').split(',')

if detect_plagiarism(text):
    print("Plagiarism detected!")
else:
    print("No plagiarism detected.")
