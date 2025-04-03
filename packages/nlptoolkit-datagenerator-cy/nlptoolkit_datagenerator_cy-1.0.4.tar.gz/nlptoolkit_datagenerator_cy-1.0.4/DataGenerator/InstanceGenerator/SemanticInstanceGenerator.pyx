from AnnotatedSentence.AnnotatedSentence cimport AnnotatedSentence
from AnnotatedSentence.AnnotatedWord cimport AnnotatedWord
from Classification.Instance.CompositeInstance cimport CompositeInstance
from WordNet.SynSet cimport SynSet


cdef class SemanticInstanceGenerator(SimpleWindowInstanceGenerator):

    def __init__(self,
                 fsm: FsmMorphologicalAnalyzer,
                 wordNet: WordNet):
        """
        Constructor for the semantic instance generator. Takes morphological analyzer and wordnet as input to set the
        corresponding variables.

        PARAMETERS
        ----------
        fsm : FsmMorphologicalAnalyzer
            Morphological analyzer to be used.
        wordNet : WordNet
            Wordnet to be used.
        """
        self.__fsm = fsm
        self.__word_net = wordNet

    cpdef addAttributesForWords(self,
                                Instance current,
                                Sentence sentence,
                                int wordIndex):
        """
        Generates a single classification instance of the WSD problem for the given word of the given sentence. If the
        word has not been labeled with sense tag yet, the method returns null. In the WSD problem, the system also
        generates and stores all possible sense labels for the current instance. In this case, a classification
        instance will not have all labels in the dataset, but some subset of it.

        PARAMETERS
        ----------
        sentence : Sentence
            Input sentence.
        wordIndex : int
            The index of the word in the sentence.

        RETURNS
        -------
        Instance
            Classification instance.
        """
        pass

    cpdef addAttributesForEmptyWords(self,
                                     Instance current,
                                     str emptyWord):
        pass

    cpdef Instance generateInstanceFromSentence(self,
                                                Sentence sentence,
                                                int wordIndex):
        cdef list possible_syn_sets, possible_class_labels
        cdef AnnotatedWord word
        cdef str class_label
        cdef CompositeInstance current
        cdef SynSet syn_set
        if isinstance(sentence, AnnotatedSentence):
            possible_syn_sets = sentence.constructSynSets(self.__word_net, self.__fsm, wordIndex)
            word = sentence.getWord(wordIndex)
            if isinstance(word, AnnotatedWord):
                class_label = word.getSemantic()
                current = CompositeInstance(class_label)
                possible_class_labels = []
                for synSet in possible_syn_sets:
                    possible_class_labels.append(synSet.getId())
                current.setPossibleClassLabels(possible_class_labels)
                self.addAttributes(current, sentence, wordIndex)
                return current
