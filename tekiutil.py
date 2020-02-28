import os
from gensim.utils import simple_preprocess

def listFiles(dirName):
    """
    list paths to all files in directory tree in parent directory
    Parameters:
        dirName: str of parent directory
    """
    listFile = os.listdir(dirName)
    allFiles = list()
    for entry in listFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + listFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

#TODO: preprocessing tokenizer classe
def sentTokenizer(sents, deacc=False):
    """ generator tokenizer for list of strs
    - deacc: default False with punctuation, True without
    """
    assert type(sents) == list, "Input has to be list"

    for sent in sents:
        yield (simple_preprocess(str(sent), deacc=deacc))

def docTokenizer(docs, deacc=False):
    """ Tokenize list of strings and return list of list of unigrams
    - deacc: default False with punctuation, True without
    """
    assert type(docs) == list, "Input has to be list"
    
    return list(sentTokenizer(docs, deacc=deacc))