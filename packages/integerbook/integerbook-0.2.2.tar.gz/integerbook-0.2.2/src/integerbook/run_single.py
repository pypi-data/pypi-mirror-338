import music21
from integerbook.parser.main_parser import MainParser
from integerbook.plotter.main_plotter import MainPlotter

# stream_obj = music21.converter.parse("tinynotation: 4/4 c d e c e f# g2 '")

p1 = "simple.musicxml"
p2 = "/Users/jvo/Downloads/All_Of_Me.musicxml"

file_path = p2


parser = MainParser(file_path)
sheet = parser.parse_stream()

# Create visualization
plotter = MainPlotter(sheet)
plotter.plot()
plotter.save(f'/Users/jvo/Downloads/output/simple.pdf')
#
# Save JSON
json_file_path = '/Users/jvo/Documents/programming/swift/integerbook/integerbook/sheet2.json'
sheet.save_to_json(json_file_path)
print(sheet.to_json())
