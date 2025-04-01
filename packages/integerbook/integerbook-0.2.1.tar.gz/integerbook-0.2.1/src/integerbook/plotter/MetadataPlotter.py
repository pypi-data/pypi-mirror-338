from integerbook.plotter.base_plotter import BasePlotter

class MetadataPlotter(BasePlotter):

    def plot_metadata(self):
        if not self.PlotSettings.scroll:
            self._plot_title()
            self._plot_composer()
            self._plot_arranger()
            self._plot_key_origin()


    def _plot_title(self):

        self.CanvasManager.add_text(0, 0.5, self.PlotSettings.y_pos_title,
                     self.sheet.title, fontsize=16, ha='center',
                     va='top')

    def _plot_composer(self):
        if self.sheet.arranger == "" or not self.PlotSettings.plot_arranger:
            height = self.PlotSettings.y_pos_arranger
        else:
            height = self.PlotSettings.y_pos_composer

        self.CanvasManager.add_text(0, 1 - self.XLocationFinder.get_x_margin_metadata(), height,
                          self.sheet.composer, fontsize=self.PlotSettings.font_size_metadata, ha='right',
        va='baseline')


    def _plot_arranger(self):
        if self.PlotSettings.plot_arranger:
            self.CanvasManager.add_text(0, 1 - self.XLocationFinder.get_x_margin_metadata(), self.PlotSettings.y_pos_arranger,
                          self.sheet.arranger, fontsize=self.PlotSettings.font_size_metadata, ha='right',
                          va='baseline')

    def _plot_key_origin(self):
        key_origin = self.sheet.key_origins[0].origin

        self.CanvasManager.add_text(0, self.XLocationFinder.get_x_margin_metadata(), self.PlotSettings.y_pos_arranger,
                     f"1 = {key_origin}", fontsize=self.PlotSettings.font_size_metadata,
                     ha='left',
                     va='baseline')


