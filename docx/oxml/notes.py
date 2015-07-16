from .xmlchemy import BaseOxmlElement, qn


class CT_Notes(BaseOxmlElement):
    _notes_tag = None

    @property
    def notes_lst(self):
        return self.findall(self._notes_tag)


class CT_Endnotes(CT_Notes):
    _notes_tag = qn('w:endnote')


class CT_Footnotes(CT_Notes):
    _notes_tag = qn('w:footnote')


class CT_FtnEdn(BaseOxmlElement):

    @property
    def type(self):
        return self.attrib.get(qn('w:type'))

    @property
    def id(self):
        return int(self.attrib.get(qn('w:id')))

    @property
    def p_lst(self):
        return self.findall(qn('w:p'))


class CT_FtnEdnRef(BaseOxmlElement):

    @property
    def id(self):
        return int(self.attrib.get(qn('w:id')))


class CT_EndnoteReference(CT_FtnEdnRef):
    pass


class CT_FootnoteReference(CT_FtnEdnRef):
    pass
