# Python script for parsing content in "train 2.tsv"
import numpy as np
import csv
from math import log

# only compute representations for sentences (and not included subphrases)
only_sentences = True

# do one pass through to calculate idf
word_idfs = {}
num_docs = 0
with open("train 2.tsv", 'rb') as phrasedata:
    tsvin = csv.reader(phrasedata, delimiter='\t')
    headers = tsvin.next()
    for (_, _, phrase, _) in tsvin:
    	num_docs += 1
        for word in set(phrase.split()):
            if word not in word_idfs:
                word_idfs[word] = 0
            word_idfs[word] += 1

num_words = len(word_idfs)
print "There were {0} words and {1} docs".format(num_words, num_docs)

# construct mapping from words to word id
word_ids = {}
id = 0
for word in word_idfs:
    word_ids[word] = id
    id += 1

# prepare output files
if only_sentences:
    tfidf_file = "sentences_tfidf.csv"
    raw_counts_file = "sentences_raw_counts.csv"
else:
    tfidf_file = "phrases_tfidf.csv"
    raw_counts_file = "phrases_raw_counts.csv"

tfidf_output = open(tfidf_file, "w")
raw_counts_output = open(raw_counts_file, "w")

tfidf_writer = csv.writer(tfidf_output)
raw_counts_writer = csv.writer(raw_counts_output)

# do another pass, this time constructing
with open("train 2.tsv", 'rb') as phrasedata:
    tsvin = csv.reader(phrasedata, delimiter='\t')
    headers = tsvin.next()
    
    prev_sentenceid = -1
    for (phraseid, sentenceid, phrase, sentiment) in tsvin:
        if only_sentences and prev_sentenceid == sentenceid:
            continue
        prev_sentenceid = sentenceid

        word_counts = {}
        for word in phrase.split():
            if word not in word_counts:
                word_counts[word] = 0
            word_counts[word] += 1

        # compute representation
        tfidf = [0] * num_words
        raw_counts = [0] * num_words
        for word, count in word_counts.iteritems():
            tfidf[word_ids[word]] = count / log(float(num_docs) / word_idfs[word])
            raw_counts[word_ids[word]] = count
        
        tfidf_writer.writerow([phraseid, sentiment] + tfidf)
        raw_counts_writer.writerow([phraseid, sentiment] + raw_counts)

tfidf_output.close()
raw_counts_output.close()


