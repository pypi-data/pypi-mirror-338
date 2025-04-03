from NamedEntityRecognition.NamedEntityType import NamedEntityType
from AnnotatedSentence.AnnotatedWord cimport AnnotatedWord


cdef class NerInstanceGenerator(SimpleWindowInstanceGenerator):

    cpdef addAttributesForWords(self,
                                Instance current,
                                Sentence sentence,
                                int wordIndex):
        pass

    cpdef addAttributesForEmptyWords(self,
                                     Instance current,
                                     str emptyWord):
        pass

    cpdef Instance generateInstanceFromSentence(self,
                                                Sentence sentence,
                                                int wordIndex):
        cdef AnnotatedWord word
        cdef str class_label
        cdef Instance current
        word = sentence.getWord(wordIndex)
        if isinstance(word, AnnotatedWord):
            class_label = NamedEntityType.getNamedEntityString(word.getNamedEntityType())
            current = Instance(class_label)
            self.addAttributes(current, sentence, wordIndex)
            return current
