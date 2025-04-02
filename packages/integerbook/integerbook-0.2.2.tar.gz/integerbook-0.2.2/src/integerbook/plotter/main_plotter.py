
from integerbook.canvas.canvas_manager import CanvasManager
from integerbook.plotter.note_plotter import NotePlotter


class MainPlotter:
    def __init__(self, sheet):

        self.sheet = sheet

        self.CanvasManager = CanvasManager()
        self.CanvasManager.create_canvas(1)


    def save(self, path_name):
        self.CanvasManager.save(path_name)

    def plot(self):
        NotePlotter(self.sheet, self.CanvasManager).plot_notes()
