from abc import abstractmethod, ABCMeta

from nltk.corpus import reuters
from sklearn.datasets import fetch_20newsgroups


class DataProvider(metaclass=ABCMeta):
    @abstractmethod
    def get_documents(self, start_index=0, end_index=-1): pass


class ReutersDataProvider(DataProvider):
    def get_documents(self, start_index=0, end_index=-1):
        ctgs = reuters.categories()[start_index:end_index]

        train, train_ctg = [], []
        test, test_ctg = [], []
        for category in ctgs:
            fields = reuters.fileids(categories=[category])
            for doc_id in fields:
                if doc_id.startswith('train'):
                    train = train + [reuters.raw(doc_id)]
                    train_ctg = train_ctg + [category]
                if doc_id.startswith('test'):
                    test = test + [reuters.raw(doc_id)]
                    test_ctg = test_ctg + [category]

        return train, train_ctg, test, test_ctg


class NewsgroupsDataProvider(DataProvider):
    def get_documents(self, start_index=0, end_index=-1):
        train = fetch_20newsgroups(subset='train')
        test = fetch_20newsgroups(subset='test')

        return train.data, train.target, test.data, test.target