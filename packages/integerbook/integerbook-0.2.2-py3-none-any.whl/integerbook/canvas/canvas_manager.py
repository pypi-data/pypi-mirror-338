from matplotlib.figure import Figure
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle



class CanvasManager:
    def __init__(self):
        self.figs = []
        self.axs = []
        self.width_a4 = 8.27
        self.height_a4 = 11.69
        self.xy_ratio = self.width_a4 / self.height_a4


    def create_canvas(self, num_pages=1):
        for _ in range(num_pages):
            fig = Figure(figsize=(self.width_a4, self.height_a4))
            ax = fig.subplots()
            ax = self._format_ax(ax)
            self.figs.append(fig)
            self.axs.append(ax)

    def _format_ax(self, ax):
        ax.set_ylim(0, 1)
        ax.set_xlim(0, 1)
        ax.axis('off')
        ax.set_position([0, 0, 1, 1])
        return ax

    def save(self, path_name):
        with PdfPages(path_name) as pdf:
            for fig in self.figs:
                pdf.savefig(fig)

    def create_rectangle(self, x, y, width, height):
        patch = Rectangle((x,y), width, height)
        self.axs[0].add_patch(patch)