from AnnotatedTree.ParseTreeDrawable cimport ParseTreeDrawable
from AnnotatedTree.TreeBankDrawable cimport TreeBankDrawable
from Classification.DataSet.DataSet cimport DataSet
from DataGenerator.InstanceGenerator.InstanceGenerator cimport InstanceGenerator


cdef class DataSetGenerator:

    cdef TreeBankDrawable __tree_bank
    cdef InstanceGenerator __instance_generator

    cpdef setInstanceGenerator(self, InstanceGenerator instanceGenerator)
    cpdef list generateInstanceListFromTree(self, ParseTreeDrawable parseTree)
    cpdef DataSet generate(self)
