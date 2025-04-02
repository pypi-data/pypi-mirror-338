import music21

from integerbook.note import Note

class NoteParser():

    def __init__(self, stream_obj):
        self.stream_obj = stream_obj
        self.lowest_midi = self._get_lowest_midi()

    def parse_notes(self):
        notes = []
        for m21_note in self.stream_obj[music21.note.Note]:
            notes.append(self._parse_note(m21_note))
        return notes

    def _parse_note(self, m21_note):
        note = Note(
            offset=float(m21_note.getOffsetInHierarchy(self.stream_obj)),
            position=m21_note.pitch.midi - self.lowest_midi,
            duration=float(m21_note.duration.quarterLength)
        )
        return note
    def _get_lowest_midi(self):
        lowest_midi = 127
        for m21_note in self.stream_obj[music21.note.Note]:
            if m21_note.pitch.midi < lowest_midi:
                lowest_midi = m21_note.pitch.midi
        return lowest_midi



