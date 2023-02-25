import sys
import json
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize
from gensim.similarities import WmdSimilarity
from pyemd import emd
import gensim

# nltk.download('omw-1.4')
# nltk.download('stopwords')
# Download data for tokenizer.
# nltk.download('punkt')
# nltk.download('wordnet')

# Initialize WmdSimilarity.
stop_words = stopwords.words('english')


def lematize_list(words):
    n = len(words)
    for i in range(n):
        w = words[i]
        words[i] = WordNetLemmatizer().lemmatize(w, 'v')
        # print( words[i])

    return words


def preprocess(doc):
    doc = doc.lower()  # Lower the text.
    doc = word_tokenize(doc)  # Split into words.
    doc = [w for w in doc if not w in stop_words]  # Remove stopwords.
    doc = [w for w in doc if w.isalpha()]  # Remove numbers and punctuation.
    return doc


# read file
with open('hadis.json', 'r') as myfile:
    data = myfile.read()
data = data[data.find('['):]
hadis = json.loads(data)
# print(hadis[0])

#
instance = WmdSimilarity.load('models/web-file')
# sent = 'is Friday prayer mandatory for women and sick person ?'
sent = sys.argv[1]
# print(sent)
query = preprocess(sent)
# print(query)
sims = instance[query]
# print(sims)

# Print the query and the retrieved documents, together with their similarities.
print()
print('Query : ', sent)
print()
for i in range(2):
    # print ( "Similarity = " , ( sims[i][1] ) )
    print(hadis[sims[i][0]]['hadis'])
    print("Reference : ", hadis[sims[i][0]]['reference'])
    print()
