# Naive Bayes classifier for the Rotten tomatoes sentiment data
import re, string
from math import log, exp
class NaiveBayesClassifier:
    
    def __init__(self, labels, ngrams=1):
        self.features = {}
        self.labels = labels
        self.ngrams = ngrams
        self.normalize_pattern = re.compile('[^a-zA-Z0-9\s]+')

    def add_example(self, example, label):
        ngrams = self._extract_features(example)

        for feature in ngrams:
            if feature not in self.features:
                self.features[feature] = {label:0 for label in self.labels}
            self.features[feature][label] += 1

    def sanitize_features(self, threshold=5):
        """ remove features with fewer than threshold occurences """
        for feature, labels in self.features.items():
            if sum(labels.values()) <= threshold:
                del self.features[feature]

    def predict(self, example, return_probabilities=False):
        ngrams = self._extract_features(example)

        label_probs = {label:0 for label in self.labels}
        for feature in ngrams:
            if feature not in self.features:
                continue
            label_counts = self.features[feature]
            feature_count = float(sum(label_counts))
            zero_count_labels = set([])
            for label, label_count in label_counts.iteritems():
                if label_count == 0:
                    zero_count_labels.add(label_count)
                else:
                    label_probs[label] += log(label_count / feature_count)
            
        max_value = max(label_counts.values())
        for label in label_probs:
            if label_probs[label] == max_value:
                return label
               
    def _extract_features(self, example):
        words = self.normalize_pattern.sub(example, example).split()
        
        # compute ngrams with some list comprehension magic
        return zip(*[words[i:] for i in range(self.ngrams)])


