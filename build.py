# NLTK import
from gensim.similarities import WmdSimilarity
from pyemd import emd
import gensim.downloader as api
from gensim.models.word2vec import Word2Vec
import gensim
import json
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
#
stop_words = stopwords.words('english')
# Initialize WmdSimilarity.

# read file
with open('hadis.json', 'r') as myfile:
    data = myfile.read()

data = data[data.find('['):]
hadis = json.loads(data)
# print(hadis[0])


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


wmd_corpus = []
for i in range(len(hadis)):
    # print(hadis[i]['hadis'])
    text = preprocess(hadis[i]['hadis'])
    wmd_corpus.append(text)

model = api.load('word2vec-google-news-300')
num_best = 2
instance = WmdSimilarity(wmd_corpus, model, num_best=2)
instance.save('models/web-file')
