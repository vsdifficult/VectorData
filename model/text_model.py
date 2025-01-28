from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import csr_matrix
from transformers import BertTokenizer, BertModel
from gensim.models import KeyedVectors 
import pandas as pd, torch, numpy as np 

class TextModel:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def fit(self, documents):
        self.vectorizer.fit(documents)

    def transform(self, documents):
        return self.vectorizer.transform(documents)
    
class BertModelWrapper:
    def __init__(self, model_name='bert-base-uncased'):
        # Load the pre-trained BERT model and tokenizer
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name)
        self.model.eval()  # Set the model to evaluation mode

    def transform(self, text):
        # Tokenize the input text
        inputs = self.tokenizer(text, return_tensors='pt', padding=True, truncation=True)
        
        # Get the embeddings from the model
        with torch.no_grad():  # Disable gradient calculation
            outputs = self.model(**inputs)
        
        # The last hidden state is the first element of the output tuple
        last_hidden_state = outputs.last_hidden_state
        
        # Return the embeddings (you can choose to return the mean or the CLS token)
        return last_hidden_state.mean(dim=1)  # Mean pooling

class MicrosoftGloVe100D:
    def __init__(self, glove_file='glove.6B.100d.txt'):
        """Инициализация модели GloVe с использованием предобученной модели"""
        # Загрузка предобученной модели GloVe
        self.model = KeyedVectors.load_word2vec_format(glove_file, binary=False, no_header=True)

    def transform(self, text):
        """Преобразование текста в векторы"""
        words = text.split()
        
        word_vectors = []
        for word in words:
            if word in self.model:
                word_vectors.append(self.model[word])
        
        if word_vectors:
            return np.mean(word_vectors, axis=0)
        else:
            return np.zeros(self.model.vector_size)