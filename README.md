# Jazz Chord Identification Toolkit

This is an open-source jazz chord identification system, which aggregates the advantages of music21, mingus and scales-chords.com.

## Related Wheels

Up to 06/Jun/2022:

- mingus (0.6.1): [https://bspaans.github.io/python-mingus/](https://bspaans.github.io/python-mingus/)
- music21 (7.1.0): [https://web.mit.edu/music21/doc/index.html](https://web.mit.edu/music21/doc/index.html)
- pychord (1.0.0): [https://github.com/yuma-m/pychord](https://github.com/yuma-m/pychord)
- scales-chord.com: [https://www.scales-chords.com/chordid.php](https://www.scales-chords.com/chordid.php)

## Features

Jazz chord naming is a logical task. Although it seems that this task could be done automatically, it actually suffers biases from human preferences. 

- Example 1: given a chord [C,E,A,B,D], a jazz musician will give in a second that it is a C-sixth-ninth chord; here are the performances of the existing wheels:
- - mingus: ['Esus47|CM6']
- - music21: ('Am/CaddB,D', 'minor')
- - pychord: []

- Example 2: given a chord [C,E,B,D], a jazz musician will give in a second that it is a C-major-ninth chord; here are the performances of the existing wheels:
- 