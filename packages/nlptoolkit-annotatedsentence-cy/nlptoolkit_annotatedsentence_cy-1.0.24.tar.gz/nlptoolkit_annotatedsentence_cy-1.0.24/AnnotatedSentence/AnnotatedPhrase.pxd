from typing import Optional

from Corpus.Sentence cimport Sentence


cdef class AnnotatedPhrase(Sentence):

    cdef int __word_index
    cdef Optional[str] __tag

    cpdef int getWordIndex(self)
    cpdef str getTag(self)
