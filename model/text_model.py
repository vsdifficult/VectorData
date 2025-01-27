from sklearn.feature_extraction.text import TfidfVectorizer

class TextModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit(self, documents):
        self.vectorizer.fit(documents)

    def transform(self, documents):
        return self.vectorizer.transform(documents).toarray()