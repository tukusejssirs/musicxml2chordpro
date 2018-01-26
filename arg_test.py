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



# TODO
# - -ns and --note-spelling args on separate lines (optional)
