"""
Class for training latent semantic models
"""

class LatentSemantics:
    def __init__(self, texts, titles=False):

        self.texts = texts
        if titles:
            self.titles = titles
        else:
            self.titles = ["text_{}".format(i) for i in range(len(texts))]