from music21 import converter, chord

score = converter.parse("./song.mid")
chords = score.chordify()

for c in chords.recurse().getElementsByClass('Chord'):
    print(c.pitchedCommonName, [p.nameWithOctave for p in c.pitches])
