"""
Simple preprocesser for lemmatization with backoff chain
"""
from cltk.lemmatize.latin.backoff import BackoffLatinLemmatizer
from nltk.tokenize.punkt import PunktLanguageVars

class LemmatizerLatin:
    def __init__(self, token=True):
        self.lemmatizer = BackoffLatinLemmatizer()
        self.token = token
    
    def preprocess(self, text):
        if self.token:
            lemma = self.lemmatizer.lemmatize(text)
        else:
            plv = PunktLanguageVars()
            unigrams = plv.word_tokenize(text)
            lemma = self.lemmatizer.lemmatize(unigrams)
        
        lemma = [t[0] if t[1] == "punc" else t[1] for t in lemma]    
        
        return " ".join(lemma)