from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix

class TextModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit(self, documents):
        self.vectorizer.fit(documents)

    def transform(self, documents):
        return self.vectorizer.transform(documents)
