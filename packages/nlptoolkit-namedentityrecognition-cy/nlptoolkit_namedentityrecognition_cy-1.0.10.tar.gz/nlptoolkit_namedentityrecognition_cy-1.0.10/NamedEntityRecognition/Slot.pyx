from NamedEntityRecognition.SlotType import SlotType


cdef class Slot:

    cpdef constructor1(self, object type, str tag):
        """
        Constructor for the Slot object. Slot object stores the information about more specific entities. The slot
        type represents the beginning, inside or outside the slot, whereas tag represents the entity tag of the
        slot.
        :param type: Type of the slot. B, I or O for beginning, inside, outside the slot respectively.
        :param tag: Tag of the slot.
        """
        self.type = type
        self.tag = tag

    cpdef constructor2(self, str slot):
        """
        Second constructor of the slot for a given slot string. A Slot string consists of slot type and slot tag
        separated with '-'. For example B-Person represents the beginning of a person. For outside tagging simple 'O' is
        used.
        :param slot: Input slot string.
        """
        if slot == "O":
            self.type = SlotType.O
            self.tag = ""
        else:
            _type = slot[0:slot.find("-")]
            _tag = slot[slot.find("-") + 1:]
            if _type == "B":
                self.type = SlotType.B
            elif _type == "I":
                self.type = SlotType.I
            self.tag = _tag

    def __init__(self,
                 tag: str,
                 type: SlotType = None):
        if type is not None:
            self.constructor1(type, tag)
        else:
            self.constructor2(tag)

    cpdef object getType(self):
        return self.type

    cpdef str getTag(self):
        return self.tag

    def __str__(self) -> str:
        if self.type == SlotType.O:
            return "O"
        elif self.type == SlotType.B or self.type == SlotType.I:
            return self.type.name + "-" + self.tag
        return ""
