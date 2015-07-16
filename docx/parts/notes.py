from ..opc.constants import CONTENT_TYPE
from ..opc.oxml import parse_xml
from ..opc.part import XmlPart
from ..oxml.xmlchemy import qn
from ..text.paragraph import Paragraph


class NotesPart(XmlPart):

    @classmethod
    def load(cls, partname, content_type, blob, package):
        """
        Provides PartFactory interface for loading a numbering part from
        a WML package.
        """
        notes_elm = parse_xml(blob)
        return cls(partname, content_type, notes_elm, package)

    @classmethod
    def new(cls):
        raise NotImplementedError

    def get_note(self, note_id):
        if not hasattr(self, '_notes_map'):
            self._notes_map = dict((n.id, n) for n in self.notes)

        return self._notes_map[note_id]

    @property
    def notes(self):
        name = 'footnote'

        if self.content_type == CONTENT_TYPE.WML_ENDNOTES:
            name = 'endnote'

        return [Note(n) for n in self._element.findall(qn('w:' + name))]


class Note(object):

    def __init__(self, el):
        self._element = el
        self.id = el.attrib.get(qn('w:id'))
        self.type = el.attrib.get(qn('w:type'))

    @property
    def paragraphs(self):
        return [Paragraph(p, self) for p in self._element.findall(qn('w:p'))]
