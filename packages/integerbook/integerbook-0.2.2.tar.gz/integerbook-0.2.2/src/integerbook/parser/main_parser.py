import music21.stream

from integerbook.sheet import Sheet
from integerbook.parser.note_parser import NoteParser



class MainParser:
    def __init__(self, path_sheet):
        self.sheet = Sheet()
        self.stream_obj = music21.converter.parse(path_sheet)


    def parse_stream(self):
        self.sheet.notes = NoteParser(self.stream_obj).parse_notes()

        return self.sheet



