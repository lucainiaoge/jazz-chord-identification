from rules.intervals import *

'''
    extension markers
''' 
EXT_INT = "-interval"
EXT_2ND = "-second"
EXT_4TH = "-fourth"
EXT_6TH = "-sixth"
EXT_7TH = "-seventh"
EXT_MAJ = "-major"
EXT_DOM = "-dominant"
EXT_M7TH = "-major-seventh"
EXT_9TH = "-ninth"
EXT_M9TH = "-major-ninth"
EXT_11TH = "-11th"
EXT_M11TH = "-major-11th"
EXT_13TH = "-13th"
EXT_m13TH = "-minor-13th"
EXT_M13TH = "-major-13th"

EXT_2 = "-2"
EXT_4 = "-4"
EXT_a4 = "-#4"
EXT_b9 = "-b9"
EXT_11 = "-11"
EXT_a11 = "-#11"
EXT_a5 = "-#5"
EXT_b5 = "-b5"
EXT_b13 = "-b13"

INT2NAME = {
    0: "unison",
    INT_m2: "minor-second",
    INT_M2: "major-second",
    INT_m3: "minor-third",
    INT_M3: "major-third",
    INT_4: "fourth",
    INT_a4: "tritone",
    INT_5: "fifth",
    INT_a5: "augmented-fifth",
    INT_M6: "sixth",
    INT_m7: "minor-seventh",
    INT_M7: "major-seventh",
    INT_8: "octave",
    INT_m9: "minor-ninth",
    INT_M9: "major-ninth",
    INT_m10: "minor-third",
    INT_M10: "major-third",
    INT_11: "fourth",
    INT_a11: "tritone",
    INT_12: "fifth",
    INT_m13: "augmented-fifth",
    INT_M13: "sixth",
    INT_m14: "minor-seventh",
    INT_M14: "major-seventh"
}
INT2EXT = {
    INT_m2: "-b2",
    INT_M2: "-2",
    # no thirds
    INT_4: "-4",
    INT_a4: "-#4",
    # no fifth
    INT_a5: "-#5",
    INT_M6: "-6",
    # no seventh
    INT_m9: "-b9",
    INT_M9: "-9",
    INT_a9: "-#9",
    # no 10th
    INT_11: "-11",
    INT_a11: "-#11",
    # no 12th
    INT_m13: "-b13",
    INT_M13: "-13",
    # no 14th
}
INT2EXT_MAJ = {
    INT_m2: "-b2",
    # already considered as major2 chord
    INT_m3: "-minor3",
    INT_4: "-4",
    INT_a4: "-b5",
    # no fifth
    INT_a5: "-#5",
    # no sixth, already considered as individual chord
    # no seventh
    INT_m9: "-b9",
    INT_M9: "-9",
    INT_a9: "-#9",
    # no 10th
    INT_11: "-11",
    INT_a11: "-#11",
    # no 12th
    INT_m13: "-b13",
    INT_M13: "-13",
    # no 14th
}
INT2EXT_MAJ_a4 = {
    INT_m2: "-b2",
    INT_M2: "-2",
    INT_m3: "-minor3",
    INT_4: "-4",
    # no fifth, it will be maj-#4
    # no #5, it will be aug-#4
    # no M-sixth, it will be half-dim
    # no seventh
    INT_m9: "-b9",
    INT_M9: "-9",
    INT_a9: "-#9",
    # no 10th
    INT_11: "-11",
    # no 12th, it will be maj-#4
    # no #12, it will be aug-#4
    # no M-13th, it will be half-dim
    # no 14th
}
INT2EXT_MIN = {
    INT_m2: "-b2",
    INT_M2: "-2",
    INT_M3: "-major3",
    INT_4: "-4",
    INT_a4: "-b5",
    # no fifth
    INT_a5: "-#5",
    # no sixth, already considered as individual chord
    # no seventh
    INT_m9: "-b9",
    INT_M9: "-9",
    INT_M10: "-major10",
    INT_11: "-11",
    INT_a11: "-#11",
    # no 12th
    INT_m13: "-b13",
    INT_M13: "-13",
    # no 14th
}
INT2EXT_MIN_4 = {
    INT_M2: "-2",
    INT_M3: "-major3",
    # no #4(b5), it will be dim-4
    # no fifth
    # no sixth
    INT_M7: "-seventh",
    INT_m9: "-b9",
    INT_M9: "-9",
    INT_M10: "-major3",
    # no #11, it will be dim-4
    # no 12th
    # no 13th
    # no 14th
}
INT2EXT_DOM = {
    INT_m2: "-b2",
    INT_M2: "-9",
    INT_m3: "-#9",
    INT_4: "-11",
    INT_a4: "-#11",
    INT_a5: "-#5",
    INT_M6: "-13",
    INT_M7: "-major7",
    INT_m9: "-b9",
    INT_M9: "-9",
    INT_a9: "-#9",
    # no 10th
    INT_11: "-11",
    INT_a11: "-#11",
    INT_a12: "-b13",
    INT_M13: "-13",
    # no 14th
}
INT2EXT_DOM_a5 = {
    INT_m2: "-b2",
    INT_M2: "-9",
    INT_m3: "-#9",
    INT_4: "-11",
    INT_a4: "-#11",
    INT_M6: "-13",
    INT_M7: "-major7",
    INT_m9: "-b9",
    INT_M9: "-9",
    INT_a9: "-#9",
    # no 10th
    INT_11: "-11",
    INT_a11: "-#11",
    INT_M13: "-13",
    # no 14th
}
INT2EXT_DOM_b5 = {
    INT_m2: "-b2",
    INT_M2: "-9",
    INT_m3: "-#9",
    INT_4: "-11",
    INT_a5: "-#5",
    INT_M6: "-13",
    INT_M7: "-major7",
    INT_m9: "-b9",
    INT_M9: "-9",
    INT_a9: "-#9",
    # no 10th
    INT_11: "-11",
    INT_a12: "-b13",
    INT_M13: "-13",
    # no 14th
}
INT2EXT_SUS = {
    INT_m2: "-b2",
    # no 3th
    INT_a4: "-#11",
    INT_a5: "-#5",
    INT_M6: "-13",
    INT_M7: "-major7",
    INT_m9: "-b9",
    # no 10th
    INT_a11: "-#11",
    INT_a12: "-b13",
    INT_M13: "-13",
    # no 14th
}
INT2EXT_AUG = {
    # no b2, becuase it is inversion min-maj
    INT_M2: "-2",
    # no minor thirds, because is is inversion aug-maj
    INT_4: "-11",
    INT_a4: "-#11",
    INT_5: "-add5",
    INT_M6: "-13",
    # no seventh
    INT_m9: "-b9",
    INT_M9: "-9",
    INT_a9: "-#9",
    # no tenth
    INT_11: "-11",
    INT_a11: "-#11",
    INT_12: "-add5",
    INT_M13: "-13",
    # no 14th
}
INT2EXT_AUG_M7 = {
    # no b2, becuase it is inversion min-maj
    INT_M2: "-2",
    INT_a2: "-#9",
    INT_4: "-11",
    INT_a4: "-#11",
    INT_5: "-add5",
    INT_M6: "-13",
    # no seventh
    INT_m9: "-b9",
    INT_M9: "-9",
    INT_a9: "-#9",
    # no tenth
    INT_11: "-11",
    INT_a11: "-#11",
    INT_12: "-add5",
    INT_M13: "-13",
    # no 14th
}
INT2EXT_DIM = {
    INT_m2: "-b2",
    INT_M2: "-9",
    INT_M3: "-major3",
    INT_4: "-11",
    INT_5: "-add5",
    INT_a5: "-b13",
    # no sixth
    INT_M7: "-major7",
    INT_m9: "-b9",
    INT_M9: "-9",
    # 10th = 3th
    INT_11: "-11",
    INT_12: "-add5",
    INT_a12: "-b13",
    # no 13th
    # 14th = 7th
}
INT2EXT_DIM_M7 = {
    INT_m2: "-b2",
    INT_M2: "-9",
    INT_M3: "-major3",
    INT_4: "-11",
    INT_5: "-add5",
    INT_a5: "-b13",
    # no sixth
    # no seventh
    INT_m9: "-b9",
    INT_M9: "-9",
    # 10th = 3th
    INT_11: "-11",
    INT_12: "-add5",
    INT_a12: "-b13",
    # no 13th
    # 14th = 7th
}
INT2EXT_HALFDIM = {
    INT_m2: "-b2",
    INT_M2: "-9",
    INT_M3: "-major3",
    INT_4: "-11",
    INT_5: "-add5",
    INT_a5: "-b13",
    INT_M6: "-13",
    INT_M7: "-major7",
    INT_m9: "-b9",
    INT_M9: "-9",
    # 10th = 3th
    INT_11: "-11",
    INT_12: "-add5",
    INT_a12: "-b13",
    INT_M13:"-13"
    # 14th = 7th
}
INT2EXT_ALT = {
    INT_m2: "-b2",
    INT_M2: "-2",
    INT_4: "-11",
    INT_M6: "-13",
    # no seventh
    INT_M9: "-9",
    INT_11: "-11",
    INT_12: "-add5",
    INT_M13: "-13",
    # no 14th
}

POSSIBLE_INT2EXTS = INT2EXT.copy()
POSSIBLE_INT2EXTS.update(INT2EXT_MAJ)
POSSIBLE_INT2EXTS.update(INT2EXT_MIN)
POSSIBLE_INT2EXTS.update(INT2EXT_AUG)
POSSIBLE_INT2EXTS.update(INT2EXT_DIM)
POSSIBLE_EXTS = POSSIBLE_INT2EXTS.values()

'''
    chord qualities
'''
UNK_CHORD = "unknown"
# Majors
MAJOR = "major"
MAJOR_INT = MAJOR + EXT_INT
MAJOR_2 = MAJOR + EXT_2
MAJOR_4 = MAJOR + EXT_4
MAJOR_b5 = MAJOR + EXT_b5
MAJOR_a5 = MAJOR + EXT_a5
MAJOR_a4 = MAJOR + EXT_a4
MAJOR_6 = MAJOR + EXT_6TH
MAJOR_7 = MAJOR + EXT_7TH
MAJOR_9 = MAJOR + EXT_9TH
MAJOR_67 = MAJOR + EXT_6TH + EXT_7TH
MAJOR_69 = MAJOR + EXT_6TH + EXT_9TH
MAJOR_6_11 = MAJOR + EXT_6TH + EXT_11TH
MAJOR_6_a11 = MAJOR + EXT_6TH + EXT_a11
MAJOR_11 = MAJOR + EXT_11TH
MAJOR_a11 = MAJOR + EXT_7TH + EXT_a11
MAJOR_13 = MAJOR + EXT_13TH
MAJOR_13_a11 = MAJOR + EXT_13TH + EXT_a11
# Minors
MINOR = "minor"
MINOR_INT = MINOR + EXT_INT
MINOR_4 = MINOR + EXT_4
MINOR_6 = MINOR + EXT_6TH
MINOR_7 = MINOR + EXT_7TH
MINOR_67 = MINOR + EXT_6TH + EXT_7TH
MINOR_9 = MINOR + EXT_9TH
MINOR_69 = MINOR + EXT_6TH + EXT_9TH
MINOR_67 = MINOR + EXT_6TH + EXT_7TH
MINOR_6_11 = MINOR + EXT_6TH + EXT_11TH
MINOR_6_a11 = MINOR + EXT_6TH + EXT_a11
MINOR_11 = MINOR + EXT_11TH
MINOR_a11 = MINOR + EXT_a11
MINOR_13 = MINOR + EXT_13TH
MINOR_13_a11 = MINOR + EXT_13TH + EXT_a11
# Minor-majors
MINOR_M7 = MINOR + EXT_M7TH
MINOR_6_M7 = MINOR + EXT_6TH + EXT_M7TH
MINOR_69_M7 = MINOR + EXT_6TH + EXT_9TH + EXT_M7TH
MINOR_6_M11 = MINOR + EXT_6TH + EXT_11TH + EXT_M7TH
MINOR_6_M7_a11 = MINOR + EXT_6TH + EXT_M7TH + EXT_a11
MINOR_9_M7 = MINOR + EXT_9TH + EXT_M7TH
MINOR_11_M7 = MINOR + EXT_11TH + EXT_M7TH
MINOR_a11_M7 = MINOR + EXT_M7TH + EXT_a11
MINOR_13_M7 = MINOR + EXT_13TH + EXT_M7TH
MINOR_13_M7_a11 = MINOR + EXT_13TH + EXT_M7TH + EXT_a11
# Dominants
DOM = "dominant"
DOM_7 = DOM + EXT_7TH
DOM_7_a5 = DOM + EXT_7TH + EXT_a5
DOM_7_b5 = DOM + EXT_7TH + EXT_b5
DOM_9 = DOM + EXT_9TH
DOM_11 = DOM + EXT_11TH
DOM_13 = DOM + EXT_13TH
DOM_7b9 = DOM + EXT_7TH + EXT_b9
DOM_11b9 = DOM + EXT_11TH + EXT_b9
DOM_13b9 = DOM + EXT_13TH + EXT_b9
DOM_7_a11 = DOM + EXT_7TH + EXT_a11
DOM_13_a11 = DOM + EXT_13TH + EXT_a11

DOM_a5_9 = DOM + EXT_9TH + EXT_a5
DOM_a5_11 = DOM + EXT_11TH + EXT_a5
DOM_a5_13 = DOM + EXT_13TH + EXT_a5
DOM_a5_7b9 = DOM + EXT_7TH + EXT_a5 + EXT_b9
DOM_a5_11b9 = DOM + EXT_11TH + EXT_a5 + EXT_b9
DOM_a5_13b9 = DOM + EXT_13TH + EXT_a5 + EXT_b9
DOM_a5_7_a11 = DOM + EXT_7TH + EXT_a11
DOM_a5_13_a11 = DOM + EXT_13TH + EXT_a5 + EXT_a11

DOM_b5_9 = DOM + EXT_9TH + EXT_a5
DOM_b5_11 = DOM + EXT_11TH + EXT_a5
DOM_b5_13 = DOM + EXT_13TH + EXT_a5
DOM_b5_7b9 = DOM + EXT_7TH + EXT_a5 + EXT_b9
DOM_b5_11b9 = DOM + EXT_11TH + EXT_a5 + EXT_b9
DOM_b5_13b9 = DOM + EXT_13TH + EXT_a5 + EXT_b9

# Sus
SUS = "suspended"
SUS_2 = SUS + EXT_2ND
SUS_7 = SUS + EXT_7TH
SUS_M7 = SUS + EXT_M7TH
SUS_13 = SUS + EXT_13TH
SUS_M13 = SUS + EXT_MAJ + EXT_13TH
# Augmented
AUG = "augmented"
AUG_M7 = AUG + EXT_M7TH
AUG_M7_M9 = AUG + EXT_MAJ + EXT_9TH
AUG_M7_M11 = AUG + EXT_MAJ + EXT_11TH
AUG_M7_a11 = AUG + EXT_MAJ + EXT_a11
AUG_M7_M13 = AUG + EXT_MAJ + EXT_13TH
AUG_M7_M13_a11 = AUG + EXT_MAJ + EXT_13TH + EXT_a11
# Diminished
DIM = "diminished"
DIM_7 = DIM + EXT_7TH
DIM_M7 = DIM + EXT_M7TH
DIM_9 = DIM + EXT_9TH
DIM_M9 = DIM + EXT_MAJ + EXT_9TH
# Half-diminished
HALFDIM = "half-diminished"
HALFDIM_7 = HALFDIM + EXT_7TH
HALFDIM_9 = HALFDIM + EXT_9TH
HALFDIM_11 = HALFDIM + EXT_11TH
HALFDIM_b13 = HALFDIM + EXT_b13
# Altered
ALT = "alt"

# Half-dim rootless voicing grip inversions
# ROOTLESS_GRIP_1 = "rootless-type1"
# PHRIGIAN = "phrigian"
# ROOTLESS_GRIP_2 = "rootless-type2"

