"""
Class for training latent semantic models
"""
import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel

class LatentSemantics:
    def __init__(self, texts, titles=False):

        self.texts = texts
        if titles:
            self.titles = titles
        else:
            self.titles = ["text_{}".format(i) for i in range(len(texts))]

    def generate_id2word(self):
        return corpora.Dictionary(self.texts)

    def generate_corpus(self):
        id2word = self.generate_id2word()
        return [id2word.doc2bow(text) for text in self.texts]