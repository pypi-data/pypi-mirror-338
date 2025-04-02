cdef class Slot:

    cdef object type
    cdef str tag

    cpdef object getType(self)
    cpdef str getTag(self)

    cpdef constructor1(self, object type, str tag)

    cpdef constructor2(self, str slot)
