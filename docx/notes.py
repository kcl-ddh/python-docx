class NoteReference(object):
    def __init__(self, el, note_type=None):
        self._element = el

    @property
    def id(self):
        return self._element.id


class EndnoteReference(NoteReference):
    pass


class FootnoteReference(NoteReference):
    pass
