# coding=utf-8

__author__ = 'Josu Bermudez <josu.bermudez@deusto.es>'
__date__ = '11/29/12'

from logging import getLogger


class BaseDocument:
    """ The base for create a document writer.
    """
    def __init__(self, filename="", stream=None, document_id=None, logger=None):
        if logger:
            self.logger = logger
        else:
            self.logger = getLogger("documentWritter")
        self.document_id = document_id
        if stream:
            self.file = stream
        else:
            self.file = open(filename, "w")

    @staticmethod
    def store(*args):
        """Implement here the storing code.
        :param args: The arguments needed for store the graph.
        """
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
