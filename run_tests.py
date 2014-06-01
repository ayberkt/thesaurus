import thesaurus as th
import unittest


class TestSynonyms(unittest.TestCase):

    synoynms_of_nice = {'decent': ['decent', 'nice'],
                        'dainty': ['dainty', 'nice', 'overnice',
                                   'prissy', 'squeamish'],
                        'courteous': ['courteous', 'gracious', 'nice'],
                        'nice': ['nice', 'skillful']}

    def test_synonyms(self):
        self.assertEqual(th.synonyms('nice'), self.synoynms_of_nice)


class TestAntonyms(unittest.TestCase):

    def test_antonyms(self):
        pass


class TestRelatedForms(unittest.TestCase):

    def test_related_forms(self):
        pass


if __name__ == '__main__':
    unittest.main()
