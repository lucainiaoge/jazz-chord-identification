# Jazz Chord Identification Toolkit

This is an open-source jazz chord identification system, which aggregates the advantages of `music21`, `mingus` and scales-chords.com.

## Related Wheels

Up to 06/Jun/2022:

- `mingus` (0.6.1): [https://bspaans.github.io/python-mingus/](https://bspaans.github.io/python-mingus/)
- `music21` (7.1.0): [https://web.mit.edu/music21/doc/index.html](https://web.mit.edu/music21/doc/index.html)
- `pychord` (1.0.0): [https://github.com/yuma-m/pychord](https://github.com/yuma-m/pychord)
- scales-chord.com: [https://www.scales-chords.com/chordid.php](https://www.scales-chords.com/chordid.php)

## Features

### Human-preference-aware

Jazz chord naming is a logical task. It seems that this task could be done automatically with a set of simple rules. However, this is not the case. The namings of chords are subjective, and there are many preferences of musicians on chord naming. This warns: even if the naming from an automatic chord identification system is technically correct, it may not be the desired one. Here are several examples:

- Example 1: given a chord [C,E,A,B,D], a jazz musician will give in a second that it is a C-sixth-ninth chord; here are the performances of the existing wheels:
  - `mingus`: ['Esus47|CM6']
  - `music21`: ('Am/CaddB,D', 'minor')
  - `pychord`: []
  - scales-chord.com: No chord found

- Example 2: given a chord [C,E,B,D], a jazz musician will give in a second that it is a C-major-ninth chord; here are the performances of the existing wheels:
  - `mingus`: ['Em7|CM7']
  - `music21`: ('CM9', 'major-ninth')
  - `pychord`: []
  - scales-chord.com: Cmaj9

Our system is tailored on the chord naming preferences of jazz musicians. It takes account of every commonly/less-commonly used chords, at the same time avoiding overly complex naming.

### Super-fast

Our system is 30 times faster than `music21`. Although 3 times slower than `mingus` and 8 times slower than `pychord`, our system is more powerful than `mingus` and `pychord`.

### Open-source

Although scales-chord.com outperforms `music21`,`mingus` and `pychord` on chord vocabulary and accuracy, it is not open-source. Our project is free of use for everyone under licenses.