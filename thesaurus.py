from nltk.corpus import wordnet as wn
import sys
import argparse


def synonyms(word):
    '''Returns a dict in the form of
    {'category': ['syn1', 'syn2', ...]}'''
    synsets = wn.synsets(word)
    return {syn.name.split('.')[0]: wn.synset(syn.name).lemma_names
            for syn in synsets}


def antonyms(word):
    '''Return list of antonyms.'''
    return [item for sub in
            [[antonym.name for antonym in lemma.antonyms() if antonym]
            for lemma in wn.lemmas(word) if lemma.antonyms()] for item in sub]


def derivatives(word):
    '''Return a list of derivatives.'''
    return list(set([item for sub in
                    [[derivative.name for derivative
                      in lemma.derivationally_related_forms()]
                    for lemma in wn.lemmas(word)
                    if lemma.derivationally_related_forms()] for item in sub]))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--antonyms', action='store_true')
    parser.add_argument('-d', '--derivatives', action='store_true')
    parser.add_argument('word')
    parsed_args = parser.parse_args()
    print(parsed_args)
    # If run with arg use the arg, otherwise prompt for word input.
    if len(sys.argv) < 2:
        word = raw_input('Please input a word to begin look-up: ')
    else:
        word = parsed_args.word

    if parsed_args.antonyms:
        # Display antonyms
        print('\nAntonyms for "{0}"'.format(word.capitalize()))
        print('=> ' + ', '.join(antonyms(word).capitalize()))
    elif parsed_args.derivatives:
        # Display derivatives
        print('\nDerivationally-related\
        forms for "{0}"'.format(word.capitalize()))
        print('=> ' + ', '.join(derivatives(word)))
    else:
        # Display synonyms
        print('\nSynonyms for "{}"'.format(word.capitalize()))
        synonym_dict = synonyms(word)
        for meaning_category in synonym_dict:
            print('\nAs in {0}:\n'.format(meaning_category))
            print('=> ' + ', '.join(synonym_dict[meaning_category]))
