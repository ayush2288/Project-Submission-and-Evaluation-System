import re
from collections import Counter

def tokenize(text):
    # Simple tokenization by words, removing special characters and lowercasing everything
    text = re.sub(r'\W+', ' ', text.lower())
    words = text.split()
    return words

def ngrams(words, n=3):
    # Create n-grams from a list of words
    return zip(*[words[i:] for i in range(n)])

def check_plagiarism(text, reference_texts, n=3):
    # Tokenize the input text
    text_words = tokenize(text)
    text_ngrams = list(ngrams(text_words, n))

    # Compare with reference texts
    similarity_scores = []
    for ref in reference_texts:
        ref_words = tokenize(ref)
        ref_ngrams = list(ngrams(ref_words, n))
        
        # Count occurrences of each n-gram in both texts
        text_counter = Counter(text_ngrams)
        ref_counter = Counter(ref_ngrams)
        
        # Calculate the number of shared n-grams
        shared_ngrams = sum((text_counter & ref_counter).values())
        total_ngrams = sum(text_counter.values())
        
        # Calculate a simple similarity score
        similarity = (shared_ngrams / total_ngrams) * 100 if total_ngrams > 0 else 0
        similarity_scores.append(similarity)

    # Return the highest similarity score found
    return max(similarity_scores) if similarity_scores else 0

# Example Usage
reference_texts = [
    "We will develop a function that identifies common phrases between the provided text and a set of predefined texts. While this will not be as robust as a comprehensive plagiarism detection tool, it will serve as a fundamental implementation."
]

description_1 = "We will"
result = check_plagiarism(description_1, reference_texts)
print(f"Plagiarism Score: {result}%")
