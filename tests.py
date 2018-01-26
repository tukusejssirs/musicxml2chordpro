#! /usr/bin/env python3

""" Convert MusicXML to Chordpro
"""


import xml.etree.ElementTree as ET


# Translate MusicXML chord quality to Chordpro
qualities = {
   'augmented': '+',
   'diminished': 'dim',
   'diminished-seventh': 'dim7',
   'dominant': '7',
   'dominant-ninth': '9',
   'half-diminished': 'm7b5',
   'major': '' ,
   'major-seventh': 'M7',
   'minor': 'm',
   'minor-seventh': 'm7',
   'minor-sixth': 'm6',
}

# MusicXML knows the number of sharps or flats in the key signature.
# It does not know whether it is the major or relative minor key.
# We might try to guess later.
keys = {
   -7: ('Cb', 'Abmin'),
   -6: ('Gb', 'Ebmin'),
   -5: ('Db', 'Bbmin'),
   -4: ('Ab', 'Fmin'),
   -3: ('Eb', 'Cmin'),
   -2: ('Bb', 'Gmin'),
   -1: ('F', 'Dmin'),
    0: ('C', 'Amin'),
    1: ('G', 'Emin'),
    2: ('D', 'Bmin'),
    3: ('A', 'Fmin'),
    4: ('E', 'C#min'),
    5: ('B', 'G#min'),
    6: ('F#', 'D#min'),
    7: ('C#', 'A#min'),
}


alters = {
   -2: 'bb',
   -1: 'b',
    0: '',
    1: '#',
    2: '##',
}
















if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Extract chords and lyrics from MusicXML file in ChordPro format.')
    parser.add_argument('filenames', metavar='file', nargs='+', default='-', help='a MusicXML file to process')
    parser.add_argument('-ns', '--note-spelling', nargs='+', default='standard', choices=['standard', 'german', 'full-german', 'solfeggio', 'french'],
                        help='note spelling used in chord names (default: %(default)s)')
    parser.add_argument('-lm', '--lower-minor', default="false", action='store_true', help='use lower-case minor chords (default: %(default)s)')
    parser.add_argument('-lb', '--lower-bass', default="false", action='store_true', help='use lower-case bass notes (default: %(default)s)')
    parser.add_argument('-ac', '--all-caps', default="false", action='store_true', help='use all-capitol note names (default: %(default)s)')

    args = parser.parse_args()

    #import sys
    #fout = sys.stdout
    #for filename in args.filenames:
        #if filename == '-':
            #data = sys.stdin
        #else:
            #data = filename
        #x1 = XML2Pro(data, fout)
        #x1.process_file()
