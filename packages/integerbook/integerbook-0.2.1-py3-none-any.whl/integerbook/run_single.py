import music21
from integerbook.parser.main_parser import MainParser
from integerbook.plotter.main_plotter import MainPlotter

# stream_obj = music21.converter.parse("tinynotation: 4/4 c d e c e f# g2 '")

p1 = "/Users/jvo/Downloads/All_Of_Me.musicxml"
p2 = "/Users/jvo/Downloads/Autumn_Leaves_18ae0812-5600-4fcc-8a30-170c9edcd876.musicxml"
p3 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/glissando.mxl"
p4 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/hammer-on.musicxml"
p5 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/voices.musicxml"
p6 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/vibrato3.musicxml"
p7 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/gracenotes.musicxml"
p8 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/lyrics-voices.musicxml"
p9 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/lyrics-syllabic-melisma.musicxml"
p10 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/ties.musicxml"
p11 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/string-articulations2.musicxml"
p12 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/slash-chords.musicxml"
p13 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/repeat-brackets-long.musicxml"
p14 = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files-new/barlines.musicxml"
p15 = "/Users/jvo/Downloads/Lonestar.musicxml"
p16 = "/Users/jvo/Documents/programming/music-visualization-new/integerbook/tests/test-files/slurs.musicxml"
p17 = "/Users/jvo/Downloads/lonestar soundslice.xml"
p18 = "/Users/jvo/Downloads/the nearness of you.xml"

file_path = p18

# manual_secondary_chords = {(1, 0): ["ii", "III"]} # [[(measure number, chord index within measure), secondary_function, secondary_key]
manual_secondary_chords = {}

user_settings = {
    "scroll": False,
    "manual_secondary_chords": manual_secondary_chords,
    "measures_per_line": 2
}

parser = MainParser(file_path, user_settings)
sheet = parser.parse_stream()

# Create visualization
plotter = MainPlotter(sheet, user_settings)
plotter.plot()
plotter.save(f'/Users/jvo/Downloads/output/{sheet.title}.pdf')

# Save JSON
json_file_path = '/Users/jvo/Documents/programming/swift/integerbook/integerbook/sheet2.json'
sheet.save_to_json(json_file_path)
print(sheet.to_json())
