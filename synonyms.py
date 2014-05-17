from nltk.corpus import wordnet as wn
import sys


def get_synonyms(word):
    synsets = wn.synsets(word)
    return {syn.name.split('.')[0]: wn.synset(syn.name).lemma_names
            for syn in synsets}

if __name__ == '__main__':

    if len(sys.argv) < 2:
        word = raw_input('Please input a word to begin look-up: ')
    else:
        word = sys.argv[1]

    print('\nSynonyms for "{}"'.format(word.capitalize()))

    for synset in get_synonyms(word):
        print('\nAs in {}:\n'.format(synset.name.split('.')[0]))
        for lemma in wn.synset(synset.name).lemma_names:
            print('  {}'.format(lemma))
