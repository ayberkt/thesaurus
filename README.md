Thesaurus
============

Simple thesaurus from the command-line using [NLTK](https://github.com/nltk/nltk)'s WordNet interface.

## Building

```
$ pip install nltk
```

After NLTK has been installed, you may need to do additional downloads

```
$ python
>>> import nltk
>>> nltk.download()
```

## Using

```
$ python thesaurus.py good

Synonyms for "Nice"

Similar to "decent":

=> decent, nice

Similar to "dainty":

=> dainty, nice, overnice, prissy, squeamish

Similar to "courteous":

=> courteous, gracious, nice

Similar to "nice":

=> nice, skillful
```

You can also get the antonyms for a word by adding a ```--antonyms``` arg.

```
$ python thesaurus.py --antonyms nice

Antonyms for "Attractive"
=> repulsive, unattractive

```
