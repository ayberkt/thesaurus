from nltk.corpus import wordnet as wn
import sys


def synonyms(word):
    '''Returns a dict in the form of
    {'semantic identifier': ['syn1', 'syn2', ...]}'''
    synsets = wn.synsets(word)
    return {syn.name.split('.')[0]: wn.synset(syn.name).lemma_names
            for syn in synsets}

if __name__ == '__main__':

    # If run with arg use the arg, otherwise prompt for word input.
    if len(sys.argv) < 2:
        word = raw_input('Please input a word to begin look-up: ')
    else:
        word = sys.argv[1]

    print('\nSynonyms for "{}"'.format(word.capitalize()))

    synonym_dict = synonyms(word)
    for semantic_group in synonym_dict:
        print('\nAs in {0}:\n'.format(semantic_group))
        print(', '.join(synonym_dict[semantic_group]))
