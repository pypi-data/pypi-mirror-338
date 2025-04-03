from AnnotatedSentence.AnnotatedSentence cimport AnnotatedSentence
from AnnotatedSentence.AnnotatedWord cimport AnnotatedWord
from AnnotatedSentence.AnnotatedCorpus cimport AnnotatedCorpus
from DisambiguationCorpus.DisambiguatedWord cimport DisambiguatedWord
from DisambiguationCorpus.DisambiguationCorpus cimport DisambiguationCorpus

cdef class SentenceDisambiguationCorpusGenerator:

    cdef AnnotatedCorpus __annotated_corpus

    def __init__(self,
                 folder: str,
                 pattern: str):
        """
        Constructor for the DisambiguationCorpusGenerator which takes input the data directory and the pattern for the
        training files included. The constructor loads the corpus from the given directory including the given files
        the given pattern.

        PARAMETERS
        ----------
        folder : str
            Directory where the sentence files reside.
        pattern : str
            Pattern of the tree files to be included in the corpus. Use "." for all files.
        """
        self.__annotated_corpus = AnnotatedCorpus(folder, pattern)

    cpdef DisambiguationCorpus generate(self):
        """
        Creates a morphological disambiguation corpus from the corpus.

        RETURNS
        -------
        DisambiguationCorpus
            Created disambiguation corpus.
        """
        cdef DisambiguationCorpus corpus
        cdef int i
        cdef AnnotatedSentence disambiguation_sentence
        cdef AnnotatedWord annotated_word
        corpus = DisambiguationCorpus()
        for i in range(self.__annotated_corpus.sentenceCount()):
            sentence = self.__annotated_corpus.getSentence(i)
            disambiguation_sentence = AnnotatedSentence()
            for j in range(sentence.wordCount()):
                annotated_word = sentence.getWord(j)
                if isinstance(annotated_word, AnnotatedWord):
                    disambiguation_sentence.addWord(DisambiguatedWord(annotated_word.getName(),
                                                                     annotated_word.getParse()))
            corpus.addSentence(disambiguation_sentence)
        return corpus
