class NotePlotter():
    def __init__(self, sheet, CanvasManager):
        self.sheet = sheet
        self.CanvasManager = CanvasManager

    def plot_notes(self):

        for note in self.sheet.notes:
            self.CanvasManager.create_rectangle(note.offset/10 % 1, note.position / 10 % 1,
                                                note.duration/10, 0.02)



