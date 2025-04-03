from AnnotatedSentence.ViewLayerType import ViewLayerType
from AnnotatedTree.TreeBankDrawable cimport TreeBankDrawable
from AnnotatedTree.ParseTreeDrawable cimport ParseTreeDrawable
from NamedEntityRecognition.NERCorpus cimport NERCorpus
from AnnotatedSentence.AnnotatedSentence cimport AnnotatedSentence


cdef class NERCorpusGenerator:

    cdef TreeBankDrawable __tree_bank

    def __init__(self,
                 folder: str,
                 pattern: str):
        """
        Constructor for the NERCorpusGenerator which takes input the data directory and the pattern for the
        training files included. The constructor loads the treebank from the given directory including the given files
        the given pattern.

        PARAMETERS
        ----------
        folder : str
            Directory where the treebank files reside.
        pattern : str
            Pattern of the tree files to be included in the treebank. Use "." for all files.
        """
        self.__tree_bank = TreeBankDrawable(folder, pattern)

    cpdef NERCorpus generate(self):
        """
        Creates a morphological disambiguation corpus from the treeBank. Calls generateAnnotatedSentence for each parse
        tree in the treebank.

        RETURNS
        -------
        DisambiguationCorpus
            Created disambiguation corpus.
        """
        cdef NERCorpus corpus
        cdef int i
        cdef ParseTreeDrawable parse_tree
        cdef AnnotatedSentence sentence
        corpus = NERCorpus()
        for i in range(self.__tree_bank.size()):
            parse_tree = self.__tree_bank.get(i)
            if parse_tree.layerAll(ViewLayerType.NER):
                sentence = parse_tree.generateAnnotatedSentence()
                corpus.addSentence(sentence)
        return corpus
