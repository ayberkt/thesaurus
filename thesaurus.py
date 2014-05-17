from nltk.corpus import wordnet as wn
import sys
import argparse


def synonyms(word):
    '''Returns a dict in the form of
    {'semantic identifier': ['syn1', 'syn2', ...]}'''
    synsets = wn.synsets(word)
    return {syn.name.split('.')[0]: wn.synset(syn.name).lemma_names
            for syn in synsets}


def antonyms(word):
    antonyms = {}
    for lemma in wn.lemmas(word):
        if not lemma.name in antonyms:
            antonyms[lemma.name.lower()] = set([ant.name for ant in
                                                lemma.antonyms() if ant])
        else:
            antonyms[lemma.name.lower()].update([ant.name for ant
                                                 in lemma.antonyms()])
    return antonyms

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--antonyms', action='store_true')
    parser.add_argument('word')
    parsed_args = parser.parse_args()
    print(parsed_args)
    # If run with arg use the arg, otherwise prompt for word input.
    if len(sys.argv) < 2:
        word = raw_input('Please input a word to begin look-up: ')
    else:
        word = parsed_args.word

    if not parsed_args.antonyms:
        # Display synonyms
        print('\nSynonyms for "{}"'.format(word.capitalize()))
        synonym_dict = synonyms(word)
        for semantic_group in synonym_dict:
            print('\nAs in {0}:\n'.format(semantic_group))
            print(', '.join(synonym_dict[semantic_group]))
    else:
        # Display antonyms
        print('\nAntonyms for "{0}"'.format(word.capitalize()))
        antonym_dict = antonyms(word)
        for key in antonym_dict:
            print(', '.join(antonym_dict[key]))
