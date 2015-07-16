from ..opc.oxml import parse_xml
from ..opc.part import XmlPart
from ..text.paragraph import Paragraph


class NotesPart(XmlPart):

    @classmethod
    def new(cls):
        raise NotImplementedError

    def get_note(self, note_id):
        if not hasattr(self, '_notes_map'):
            self._notes_map = dict((n.id, n) for n in self.notes)
        return self._notes_map[note_id]

    @property
    def notes(self):
        return [Note(n) for n in self._element.notes_lst]


class Note(object):

    def __init__(self, el):
        self._element = el
        self.id = el.id
        self.type = el.type

    @property
    def paragraphs(self):
        return [Paragraph(p, self) for p in self._element.p_lst]
