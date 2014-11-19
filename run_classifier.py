from naive_bayes import NaiveBayesClassifier
import csv

classifier = NaiveBayesClassifier(range(5))

with open("train 2.tsv", 'rb') as phrasedata:
    tsvin = csv.reader(phrasedata, delimiter='\t')
    headers = tsvin.next()
    curriter = 1
    for (_, _, phrase, sentiment) in tsvin:
        classifier.add_example(phrase, int(sentiment))
        if curriter % 1000 == 0:
            print "nother 1000"
        curriter += 1

classifier.sanitize_features()

print "done training"
with open("test.tsv", 'rb') as phrasedata:
    tsvin = csv.reader(phrasedata, delimiter='\t')
    headers = tsvin.next()
    curritter = 1
    print "PhraseId,Sentiment"
    for (phraseid, _, phrase) in tsvin:
        label = classifier.predict(phrase)
        print "{},{}".format(phraseid, label)
