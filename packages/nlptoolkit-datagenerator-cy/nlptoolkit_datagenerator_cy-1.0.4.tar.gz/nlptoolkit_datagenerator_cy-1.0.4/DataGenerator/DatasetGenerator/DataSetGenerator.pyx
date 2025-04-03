from AnnotatedSentence.AnnotatedSentence cimport AnnotatedSentence


cdef class DataSetGenerator:

    def __init__(self,
                 folder: str,
                 pattern: str,
                 instanceGenerator: InstanceGenerator):
        """
        Constructor for the DataSetGenerator which takes input the data directory, the pattern for the training files
        included, and an instanceGenerator. The constructor loads the treebank from the given directory
        including the given files having the given pattern. If punctuations are not included, they are removed from
        the data.

        PARAMETERS
        ----------
        folder : str
            Directory where the treebank files reside.
        pattern : str
            Pattern of the tree files to be included in the treebank. Use "." for all files.
        instanceGenerator : InstanceGenerator
            The instance generator used to generate the dataset.
        """
        self.__tree_bank = TreeBankDrawable(folder, pattern)
        self.__instance_generator = instanceGenerator

    cpdef setInstanceGenerator(self, InstanceGenerator instanceGenerator):
        """
        Mutator for the instanceGenerator attribute.

        PARAMETERS
        ----------
        instanceGenerator : InstanceGenerator
            Input instanceGenerator
        """
        self.__instance_generator = instanceGenerator

    cpdef list generateInstanceListFromTree(self, ParseTreeDrawable parseTree):
        """
        The method generates a set of instances (an instance from each word in the tree) from a single tree. The method
        calls the instanceGenerator for each word in the sentence.

        PARAMETERS
        ----------
        parseTree : ParseTreeDrawable
            Parsetree for which a set of instances will be created

        RETURNS
        -------
        list
            A list of instances.
        """
        cdef list instance_list
        cdef AnnotatedSentence annotated_sentence, generated_sentence
        cdef int i
        instance_list = []
        annotated_sentence = parseTree.generateAnnotatedSentence()
        for i in range(annotated_sentence.wordCount()):
            generated_sentence = self.__instance_generator.generateInstanceFromSentence(annotated_sentence, i)
            if generated_sentence is not None:
                instance_list.append(generated_sentence)
        return instance_list

    cpdef DataSet generate(self):
        """
        Creates a dataset from the treeBank. Calls generateInstanceListFromTree for each parse tree in the treebank.

        RETURNS
        -------
        DataSet
            Created dataset.
        """
        cdef DataSet data_set
        cdef int i
        cdef ParseTreeDrawable parse_tree
        data_set = DataSet()
        for i in range(self.__tree_bank.size()):
            parse_tree = self.__tree_bank.get(i)
            data_set.addInstanceList(self.generateInstanceListFromTree(parse_tree))
        return data_set
