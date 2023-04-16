import spacy

nlp = spacy.load("en_core_web_sm")

# Define a list of complex legal terms and their simpler alternatives
term_dict = {
    "indemnify": "protect",
    "indemnification": "protection",
    "confidentiality": "privacy",
    "dispute resolution": "problem-solving",
    # add more terms as needed
}

# Load the contract or agreement text
with open("contract.txt", "r") as f:
    text = f.read()

# Use spaCy to identify the complex terms
doc = nlp(text)
for token in doc:
    if token.text.lower() in term_dict:
        # Replace the complex term with the simpler alternative
        text = text.replace(token.text, term_dict[token.text.lower()])

# Create a new file with the simplified contract or agreement text
with open("simplified_contract.txt", "w") as f:
    f.write(text)


import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.wordnet import WordNetLemmatizer



# Function to simplify a sentence
def simplify_sentence(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)

    # Lemmatize the words (reduce to their base form)
    lem_words = []
    for word in words:
        lem_words.append(WordNetLemmatizer().lemmatize(word, pos='v'))

    # Remove stop words (common words that don't add meaning)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    filtered_words = [word for word in lem_words if word.lower() not in stop_words]

    # Replace complex words with simpler synonyms
    simplified_words = []
    for word in filtered_words:
        synsets = wordnet.synsets(word)
        if synsets:
            # Choose the first synonym (most common)
            simplified_words.append(synsets[0].lemmas()[0].name())
        else:
            simplified_words.append(word)

    # Join the simplified words into a new sentence
    simplified_sentence = ' '.join(simplified_words)

    return simplified_sentence

# Example usage
text = "The quick brown fox jumped over the lazy dog."
sentences = sent_tokenize(text)
simplified_sentences = []
for sentence in sentences:
    simplified_sentence = simplify_sentence(sentence)
    simplified_sentences.append(simplified_sentence)

# Print the simplified sentences
for sentence in simplified_sentences:
    print(sentence)
