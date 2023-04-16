import spacy

nlp = spacy.load("en_core_web_sm")

# Define a list of complex legal terms and their simpler alternatives
term_dict = {
"indemnify": "protect",
"indemnification": "protection",
"confidentiality": "privacy",
"dispute resolution": "problem-solving",
"arbitration": "settling a dispute outside of court",
"breach of contract": "violation of a legal agreement",
"compensatory damages": "money awarded to make up for losses",
"consideration": "something of value exchanged for a promise",
"deposition": "a witness's sworn out-of-court testimony",
"eminent domain": "the power of the government to take private property for public use",
"equitable remedy": "a solution based on fairness rather than strict legal rules",
"indictment": "formal accusation of a crime by a grand jury",
"injunction": "court order prohibiting or requiring certain actions",
"intellectual property": "creations of the mind, such as inventions or artistic works, that are protected by law",
"lien": "a legal claim on property to secure payment of a debt",
"negligence": "failure to exercise reasonable care, resulting in harm to others",
"patent": "a legal right granted for an invention or discovery",
"preemption": "the federal government's ability to overrule state laws in certain areas",
"promissory estoppel": "a legal doctrine that enforces a promise, even if there was no formal contract",
"quid pro quo": "something given or received in exchange for something else",
"replevin": "a legal action to recover property that has been wrongfully taken",
"statute of limitations": "the time limit for filing a lawsuit after an event has occurred",
"tort": "a civil wrong, such as negligence or intentional harm, that results in harm to another person or property",
"trade secret": "confidential business information that gives a competitive advantage",
"vicarious liability": "a legal doctrine that holds one person responsible for the actions of another person or entity",
"waiver": "the voluntary relinquishment of a right or claim",
"zoning": "the regulation of land use by local governments"
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

# Print the simplified contract or agreement text
print(text)


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
text = "Despite the fact that the defendant had previously been convicted of similar crimes, the defense argued that the evidence presented in this case was insufficient to prove guilt beyond a reasonable doubt."
sentences = sent_tokenize(text)
simplified_sentences = []
for sentence in sentences:
    simplified_sentence = simplify_sentence(sentence)
    simplified_sentences.append(simplified_sentence)

# Print the simplified sentences
for sentence in simplified_sentences:
    print(sentence)
