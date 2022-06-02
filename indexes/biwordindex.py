from typing import Iterable
from . import Posting, Index


class BiWordIndex(Index):

    def __init__(self):
        # Mapping of Term (str) to List of Posting
        self._dictionary = {}

    def add_term(self, term: str, doc_id: int):
        """ Record a posting of the term """
        if term in self._dictionary.keys():
            postings = self._dictionary[term]
            if postings[-1].doc_id != doc_id: # No duplicate doc_id for same term
                print("Adding the term again: ", term)
                print("With doc_id: ", doc_id)
                postings.append(Posting(doc_id=doc_id))
        else:
            self._dictionary[term] = [Posting(doc_id=doc_id)]
            print("Added new term: ", term)
            print("With doc_id: ", doc_id)

    def get_postings(self, term: str) -> Iterable[Posting]:
        """Returns a list of Postings for all documents that contain the given term."""
        #print(self._dictionary[term])
        return self._dictionary[term] if term in self._dictionary.keys() else []

    def vocabulary(self) -> Iterable[str]:
        """ Returns a sorted vocabulary list """
        vocab = list(self._dictionary.keys())
        vocab.sort()
        return vocab
