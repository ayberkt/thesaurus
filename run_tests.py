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
        self.assertEqual(th.antonyms('evil'), ['good'])


class TestRelatedForms(unittest.TestCase):

    related_forms_for_apply = ['applicative', 'applicant', 'applicable',
                               'application', 'applier', 'applicatory']

    def test_related_forms(self):
        self.assertEqual(th.derivatives('apply'), self.related_forms_for_apply)


if __name__ == '__main__':
    unittest.main()
