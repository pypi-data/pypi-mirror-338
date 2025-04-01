from typing import List

from matplotlib.figure import Figure
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle, Ellipse

from integerbook.canvas.patches import Parallelogram


class CanvasManager:
    def __init__(self):
        self.figs = []
        self.axs = []
        self.test_fig, self.test_ax = self._create_test_fig_and_ax()
        self.cap_height_per_font_size = self.get_cap_height_per_font_size()
        self.width_a4 = 8.27
        self.height_a4 = 11.69
        self.xy_ratio = self.width_a4 / self.height_a4


    def create_canvas(self, num_pages, num_a4_widths, num_a4_heights):
        for _ in range(num_pages):
            fig = Figure(figsize=(num_a4_widths * self.width_a4, num_a4_heights * self.height_a4))
            ax = fig.subplots()
            ax = self._format_ax(ax, num_a4_widths, num_a4_heights)
            self.figs.append(fig)
            self.axs.append(ax)

    def _format_ax(self, ax, num_a4_widths, num_a4_heights):
        ax.set_ylim(1 - num_a4_heights, 1)
        ax.set_xlim(0, num_a4_widths)
        ax.axis('off')
        ax.set_position([0, 0, 1, 1])
        return ax



    def save(self, path_name):
        with PdfPages(path_name) as pdf:
            for fig in self.figs:
                pdf.savefig(fig)

    def create_rectangle(self, page_index, x, y, width, height, alpha, facecolor, hatch, shape, zorder=0.5):
        parallelogram = Parallelogram(
            left_bottom=[x,y],
            left_top=[x, y + height],
            right_bottom=[x + width, y],
            right_top=[x+width, y + height],
            alpha=alpha,
            facecolor=facecolor,
            hatch=hatch,
            shape=shape,
            zorder=zorder
        )
        self.axs[page_index].add_patch(parallelogram)

    def create_parallelogram(self, page_index, left_bottom, left_top, right_bottom, right_top, alpha, facecolor, hatch, shape, zorder=0.5):
        parallelogram = Parallelogram(
            left_bottom=left_bottom,
            left_top=left_top,
            right_bottom=right_bottom,
            right_top=right_top,
            alpha=alpha,
            facecolor=facecolor,
            hatch=hatch,
            shape=shape,
            zorder=zorder
        )
        self.axs[page_index].add_patch(parallelogram)

    def add_text(self, page_idx, x, y, text, ha='left', va='baseline', **kwargs):
        plotted_object = self.axs[page_idx].text(x, y, text, ha=ha, va=va,
                                                 **kwargs)

        bb = self._get_bb_plotted_object(plotted_object, self.axs[page_idx])
        x_pos_end = bb.extents[2]
        return x_pos_end


    def create_straight_rectangle(self, page_idx, x, y, width, height, **kwargs):
        rectangle_patch = Rectangle(
            (x,y), width, height, **kwargs
        )
        self.axs[page_idx].add_patch(rectangle_patch)

    def create_circle(self, page_idx, x, y, y_diameter, **kwargs):
        x_diameter = y_diameter * self.height_a4 / self.width_a4
        ellipse = Ellipse(
            (x,y),
            x_diameter,
            y_diameter,
            **kwargs
        )
        self.axs[page_idx].add_patch(ellipse)

    def create_circle_x_diameter(self, page_idx, x, y, x_diameter, **kwargs):
        y_diameter = x_diameter * self.width_a4 / self.height_a4
        ellipse = Ellipse(
            (x,y),
            x_diameter,
            y_diameter,
            **kwargs
        )
        self.axs[page_idx].add_patch(ellipse)



    def get_cap_height_per_font_size(self, font='DejaVu Sans'):

        plotted_object = self.test_ax.text(0, 0, "3", fontsize=1000, va='baseline', font=font)

        bb = self._get_bb_plotted_object(plotted_object, self.test_ax)
        height_number = bb.extents[3]
        return height_number / 1000

    def get_x_length_text(self, text, font_size, font="DejaVu Sans"):
        plotted_object = self.test_ax.text(0, 0, text, fontsize=font_size, va='baseline', font=font)

        bb = self._get_bb_plotted_object(plotted_object, self.test_ax)
        return bb.width

    def _get_bb_plotted_object(self, plotted_object, ax):
        renderer = ax.figure._get_renderer()
        return plotted_object.get_window_extent(renderer=renderer).transformed(ax.transData.inverted())

    def _create_test_fig_and_ax(self):
        fig = Figure(figsize=(8.27, 11.69))
        ax = fig.subplots()
        ax.set_position([0, 0, 1, 1])
        return fig, ax