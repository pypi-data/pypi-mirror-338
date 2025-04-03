cdef class SearchParameter:

    cdef object __category_determination_type
    cdef object __focus_type
    cdef object __retrieval_type
    cdef object __document_weighting
    cdef object __term_weighting
    cdef int __documents_retrieved
    cdef object __search_attributes

    cpdef object getRetrievalType(self)
    cpdef object getDocumentWeighting(self)
    cpdef object getTermWeighting(self)
    cpdef int getDocumentsRetrieved(self)
    cpdef object getCategoryDeterminationType(self)
    cpdef object getFocusType(self)
    cpdef object getSearchAttributes(self)
    cpdef setRetrievalType(self, object retrievalType)
    cpdef setDocumentWeighting(self, object documentWeighting)
    cpdef setTermWeighting(self, object termWeighting)
    cpdef setDocumentsRetrieved(self, int documentsRetrieved)
    cpdef setCategoryDeterminationType(self, object categoryDeterminationType)
    cpdef setFocusType(self, object focusType)
    cpdef setSearchAttributes(self, object searchAttributes)
