from __future__ import division
import operator
import nltk
import string

from imap import auth

from crawler import crawl_youtube, crawl_facebook, crawl_twitter, crawl_trend_youtube

mail = auth()
body = auth()[1]

# body = mail[1]



def isPunct(word):
    return len(word) == 1 and word in string.punctuation


def isNumeric(word):
    try:
        float(word) if '.' in word else int(word)
        return True
    except ValueError:
        return False


class RakeKeywordExtractor:
    def __init__(self):
        self.stopwords = set(nltk.corpus.stopwords.words())
        self.top_fraction = 1  # consider top third candidate keywords by score (sesitivity)

    def _generate_candidate_keywords(self, sentences):
        phrase_list = []
        for sentence in sentences:
            words = map(lambda x: "|" if x in self.stopwords else x,
                        nltk.word_tokenize(sentence.lower()))
            phrase = []
            for word in words:
                if word == "|" or isPunct(word):
                    if len(phrase) > 0:
                        phrase_list.append(phrase)
                        phrase = []
                else:
                    phrase.append(word)
        return phrase_list

    def _calculate_word_scores(self, phrase_list):
        word_freq = nltk.FreqDist()
        word_degree = nltk.FreqDist()
        for phrase in phrase_list:
            degree = len(filter(lambda x: not isNumeric(x), phrase)) - 1
            for word in phrase:
                word_freq.inc(word)
                word_degree.inc(word, degree)  # other words

        for word in word_freq.keys():
            word_degree[word] = word_degree[word] + word_freq[word]  # itself
        # word score = deg(w) / freq(w)
        word_scores = {}
        for word in word_freq.keys():
            word_scores[word] = word_degree[word] / word_freq[word]
        return word_scores

    def _calculate_phrase_scores(self, phrase_list, word_scores):
        phrase_scores = {}
        for phrase in phrase_list:
            phrase_score = 0
            for word in phrase:
                phrase_score += word_scores[word]
            phrase_scores[" ".join(phrase)] = phrase_score
        return phrase_scores

    def extract(self, text, incl_scores=False):
        sentences = nltk.sent_tokenize(text)
        phrase_list = self._generate_candidate_keywords(sentences)
        word_scores = self._calculate_word_scores(phrase_list)
        phrase_scores = self._calculate_phrase_scores(
            phrase_list, word_scores)
        sorted_phrase_scores = sorted(phrase_scores.iteritems(),
                                      key=operator.itemgetter(1), reverse=True)
        n_phrases = len(sorted_phrase_scores)
        if incl_scores:
            return sorted_phrase_scores[0:int(n_phrases / self.top_fraction)]
        else:
            return map(lambda x: x[0],
                       sorted_phrase_scores[0:int(n_phrases / self.top_fraction)])


def rake():
    rake = RakeKeywordExtractor()
    keywords = rake.extract(body, incl_scores = False)
    return (keywords)


list = rake()


def func_calling(name):
    if filter(lambda x: 'trend' in x, list):
        return crawl_trend_youtube()
    elif filter(lambda x: 'facebook' in x, list):
        return crawl_facebook(name)
    elif filter(lambda x: 'video' in x, list):
        return crawl_youtube(name)
    elif filter(lambda x: 'tweet' in x, list):
        return crawl_twitter(name)
    else:
        return "We coundn't fullfill your query at the moment!"
