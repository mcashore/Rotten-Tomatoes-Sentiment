# Python script for parsing content in "train 2.tsv"
import numpy as np
import csv

with open("train 2.tsv", 'rb') as phrasedata:
    tsvin = csv.reader(phrasedata, delimiter='\t')
    headers = tsvin.next()

    phrases = {}
    phrase_sentiments = {}
    words = set([])

    # read and parse all phrases
    for (phrase_id, sentence_id, phrase, sentiment) in tsvin:
        phrases[phrase_id] = phrase
        phrase_sentiments[phrase_id] = sentiment

        words_in_phrase = phrase.split()
        words.update(words_in_phrase)


    # assign each word a number
    words = list(words)

    phrase_vectors = {}
    # construct a vector for each phrase
    for phrase_id, phrase in phrases.iteritems():
        words_in_phrase = phrase.split()
        word_list = [lambda word: 1 if word in words_in_phrase else 0 for word in words]
        phrase_vectors[phrase_id] = np.array(word_list)

import pdb; pdb.set_trace();
