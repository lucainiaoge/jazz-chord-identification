import music21
from music21 import harmony
from rules.chord2scale import get_scale_suggestions, UNKNOWN_KEY
from rules.scales import PITCH_NUM_2_NAME

def find_pos_in_12(pitches):
    return [pitch % 12 for pitch in pitches]

def find_key_simple_root_type(root1, type1, root2, type2):
    key = UNKNOWN_KEY
    # V -> I, V -> i
    if (root1 - root2)%12 == 7 and ("maj" in type1 or "dom" in type1):
        if "maj" in type2:
            key = (root2)%12
        elif "min" in type2:
            key = (root2+3)%12
            
    # IV -> V, iv -> V
    elif (root1 - root2)%12 == 10 and ("maj" in type2 or "dom" in type2):
        if "maj" in type1:
            key = (root2-7)%12
        elif "min" in type1:
            key = (root2-7+3)%12

    # ii -> V
    elif (root1 - root2)%12 == 7 and ("maj" in type2 or "dom" in type2):
        if "minor-seventh" in type1 or "minor-ninth" in type1 or "minor-11th" in type1 or "minor-13th" in type1:
            key = (root2-7)%12
        elif "dim" in type1:
            key = (root2-7+3)%12
    
    # IV/iv -> I, IV/iv -> i
    '''
    elif (root1 - root2)%12 == 5:
        if ("maj" in type1 or "min" in type1) and "maj" in type2:
            key = (root2)%12
        elif ("maj" in type1 or "min" in type1) and "min" in type2:
            key = (root2+3)%12
    '''
    
    return key

def find_key_simple(this_chord, next_chord):
    c1 = music21.chord.Chord(this_chord)
    if len(next_chord) == 0:
        next_chord = this_chord[:]
    c2 = music21.chord.Chord(next_chord)
    symbol1, type1 = harmony.chordSymbolFigureFromChord(c1, includeChordType=True)
    symbol2, type2 = harmony.chordSymbolFigureFromChord(c2, includeChordType=True)
    
    return find_key_simple_root_type(c1.root().midi, type1, c2.root().midi, type2)

def detect_V_I(this_chord, next_chord):
    if len(next_chord) == 0 or len(this_chord):
        return False
    c1 = music21.chord.Chord(this_chord)
    c2 = music21.chord.Chord(next_chord)
    symbol1, type1 = harmony.chordSymbolFigureFromChord(c1, includeChordType=True)
    symbol2, type2 = harmony.chordSymbolFigureFromChord(c2, includeChordType=True)


# TODO
def find_key_given_chord_track(chords):
    keys = [UNKNOWN_KEY] * len(chords)
    current_key = UNKNOWN_KEY
    
    curser = 0
    
    
    return 0