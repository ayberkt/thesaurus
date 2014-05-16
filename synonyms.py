from nltk.corpus import wordnet as wn
import sys


def get_synonyms(word):
    synsets = wn.synsets(word)
    return [a_synset for a_synset in synsets]

if __name__ == '__main__':
        for synset in get_synonyms(sys.argv[1]):
            print 'As in %s: %s' % (synset.name.split('.')[0], wn.synset(synset.name).lemma_names)
