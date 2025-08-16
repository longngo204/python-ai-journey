"""
Day 4 - Text Processing
Goal: Practice cleaning, filtering, and transforming text data.
"""

# ===== Task 1 =====
def clean_sentences(sentences):
    """Lowercase, strip spaces, and remove punctuation from list of sentences."""
    return [sentence.lower().strip().replace(",","" )for sentence in sentences] 

# ===== Task 2 =====
def word_frequency(text):
    """Count frequency of each word in a string (ignore case)."""
    return len(text.split())

# ===== Task 3 =====
def filter_short_words(words, min_length):
    """Filter out words shorter than min_length."""
    return [word for word in words if len(word) < min_length]

# ===== Task 4 =====
def replace_words(sentence, replacements):
    """
    Replace words in sentence using replacements dict.
    Example: "I like cats" + {"cats": "dogs"} -> "I like dogs"
    """
    words = sentence.split()
    words = list(map(lambda x : replacements.get(x, x), words))
    return " ".join(words)

if __name__ == "__main__":
    print(clean_sentences([" Hello World! ", "Python, is GREAT."]))
    print(word_frequency("Python is great and python is fun"))
    print(filter_short_words(["a", "ab", "abc", "abcd"], 3))
    print(replace_words("I like cats and birds", {"cats": "dogs", "birds": "fish"}))
