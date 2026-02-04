"""Zawgyi-to-Unicode conversion rules ported from Rabbit Converter.

Rules are applied in order. Each rule is a (pattern, replacement) tuple.
Ported from: https://github.com/nicholaussaurus/Rabbit-Converter
"""

ZAWGYI_TO_UNICODE_RULES = [
    # Remove duplicate diacritics
    (r"([\u102D\u102E\u103D\u102F\u1037\u1095])\1+", r"\1"),

    # Remove zero-width space
    ("\u200B", ""),

    # Medial combinations
    ("\u103d\u103c", "\u108a"),

    # Medial HA variants -> U+103E
    ("(\u103d|\u1087)", "\u103e"),

    # Medial WA: U+103C -> U+103D
    ("\u103c", "\u103d"),

    # Medial RA variants -> U+103C
    ("(\u103b|\u107e|\u107f|\u1080|\u1081|\u1082|\u1083|\u1084)", "\u103c"),

    # Medial YA variants -> U+103B
    ("(\u103a|\u107d)", "\u103b"),

    # Asat: U+1039 -> U+103A
    ("\u1039", "\u103a"),

    # Stacked SA variants
    ("(\u1066|\u1067)", "\u1039\u1006"),

    # NGA variant
    ("\u106a", "\u1009"),

    # NYA variant
    ("\u106b", "\u100a"),

    # Stacked TTA
    ("\u106c", "\u1039\u100b"),

    # Stacked TTHA
    ("\u106d", "\u1039\u100c"),

    # Stacked DDA + DDA
    ("\u106e", "\u100d\u1039\u100d"),

    # Stacked DDA + DDHA
    ("\u106f", "\u100d\u1039\u100e"),

    # Stacked NNA
    ("\u1070", "\u1039\u100f"),

    # Stacked TA variants
    ("(\u1071|\u1072)", "\u1039\u1010"),

    # Stacked KA
    ("\u1060", "\u1039\u1000"),

    # Stacked KHA
    ("\u1061", "\u1039\u1001"),

    # Stacked GA
    ("\u1062", "\u1039\u1002"),

    # Stacked GHA
    ("\u1063", "\u1039\u1003"),

    # Stacked CA
    ("\u1065", "\u1039\u1005"),

    # Stacked JA
    ("\u1068", "\u1039\u1007"),

    # Stacked JHA
    ("\u1069", "\u1039\u1008"),

    # Stacked THA variants
    ("(\u1073|\u1074)", "\u1039\u1011"),

    # Stacked DA
    ("\u1075", "\u1039\u1012"),

    # Stacked DHA
    ("\u1076", "\u1039\u1013"),

    # Stacked NA
    ("\u1077", "\u1039\u1014"),

    # Stacked PA
    ("\u1078", "\u1039\u1015"),

    # Stacked PHA
    ("\u1079", "\u1039\u1016"),

    # Stacked BA
    ("\u107a", "\u1039\u1017"),

    # Stacked MA
    ("\u107c", "\u1039\u1019"),

    # Stacked LA
    ("\u1085", "\u1039\u101c"),

    # Tall AA -> U+102F
    ("\u1033", "\u102f"),

    # Tall AA variant -> U+1030
    ("\u1034", "\u1030"),

    # Another U variant -> U+1030
    ("\u103f", "\u1030"),

    # Great SA -> U+103F
    ("\u1086", "\u103f"),

    # Reorder anusvara and medial HA+U
    ("\u1036\u1088", "\u1088\u1036"),

    # Medial HA + U combination
    ("\u1088", "\u103e\u102f"),

    # Medial HA + UU combination
    ("\u1089", "\u103e\u1030"),

    # Medial WA + HA combination
    ("\u108a", "\u103d\u103e"),

    # Reorder kinzi and medial YA
    ("\u103B\u1064", "\u1064\u103B"),

    # Reorder medial RA + consonant + kinzi
    ("\u103c([\u1000-\u1021])([\u1064\u108b\u108d])", "\\1\u103c\\2"),

    # Kinzi basic form
    ("(\u1031)?([\u1000-\u1021\u1040-\u1049])(\u103c)?\u1064", "\u1004\u103a\u1039\\1\\2\\3"),

    # Kinzi + vowel I
    ("(\u1031)?([\u1000-\u1021])(\u103b|\u103c)?\u108b", "\u1004\u103a\u1039\\1\\2\\3\u102d"),

    # Kinzi + vowel II
    ("(\u1031)?([\u1000-\u1021])(\u103b)?\u108c", "\u1004\u103a\u1039\\1\\2\\3\u102e"),

    # Kinzi + anusvara
    ("(\u1031)?([\u1000-\u1021])([\u103b\u103c])?\u108d", "\u1004\u103a\u1039\\1\\2\\3\u1036"),

    # Vowel I + anusvara combination
    ("\u108e", "\u102d\u1036"),

    # NA variant
    ("\u108f", "\u1014"),

    # RA variant
    ("\u1090", "\u101b"),

    # NNA + DDA stacked
    ("\u1091", "\u100f\u1039\u100d"),

    # TTA + TTHA stacked
    ("\u1092", "\u100b\u1039\u100c"),

    # Special MA + BBA combination
    ("\u1019\u102c(\u107b|\u1093)", "\u1019\u1039\u1018\u102c"),

    # Stacked BHA variants
    ("(\u107b|\u1093)", "\u1039\u1018"),

    # Dot below variants -> U+1037
    ("(\u1094|\u1095)", "\u1037"),

    # Reorder consonant + dot + AI
    ("([\u1000-\u1021])\u1037\u1032", "\\1\u1032\u1037"),

    # Stacked TA + medial WA combination
    ("\u1096", "\u1039\u1010\u103d"),

    # Stacked TTA + TTA
    ("\u1097", "\u100b\u1039\u100b"),

    # Reorder medial RA + consonant
    ("\u103c([\u1000-\u1021])([\u1000-\u1021])?", "\\1\u103c\\2"),

    # Reorder consonant + medial RA + medial YA
    ("([\u1000-\u1021])\u103c\u103a", "\u103c\\1\u103a"),

    # Digit 7 -> RA in certain contexts
    ("\u1047(?=[\u102c-\u1030\u1032\u1036-\u1038\u103d\u103e])", "\u101b"),

    # E vowel + digit 7 -> E vowel + RA
    ("\u1031\u1047", "\u1031\u101b"),

    # Digit 0 -> WA in certain contexts
    ("\u1040(\u102e|\u102f|\u102d\u102f|\u1030|\u1036|\u103d|\u103e)", "\u101d\\1"),

    # Digit 0 + AA -> WA + AA (not after digits)
    ("([^\u1040\u1041\u1042\u1043\u1044\u1045\u1046\u1047\u1048\u1049])\u1040\u102b", "\\1\u101d\u102b"),

    # Digit 0 + AA -> WA + AA (after digits, not followed by visarga)
    ("([\u1040\u1041\u1042\u1043\u1044\u1045\u1046\u1047\u1048\u1049])\u1040\u102b(?!\u1038)", "\\1\u101d\u102b"),

    # Digit 0 at start + AA -> WA
    ("^\u1040(?=\u102b)", "\u101d"),

    # Digit 0 + vowel I -> WA + vowel I (not before space+slash)
    ("\u1040\u102d(?!\u0020?/)", "\u101d\u102d"),

    # Digit 0 -> WA (between non-digits)
    ("([^\u1040-\u1049])\u1040([^\u1040-\u1049\u0020]|[\u104a\u104b])", "\\1\u101d\\2"),

    # Digit 0 -> WA (before newline, not after digit)
    ("([^\u1040-\u1049])\u1040(?=[\\f\\n\\r])", "\\1\u101d"),

    # Digit 0 -> WA (at end, not after digit)
    ("([^\u1040-\u1049])\u1040$", "\\1\u101d"),

    # Reorder E vowel after consonant and medials
    ("\u1031([\u1000-\u1021\u103f])(\u103e)?(\u103b)?", "\\1\\2\\3\u1031"),

    # Reorder E vowel after consonant and remaining medials
    ("([\u1000-\u1021])\u1031([\u103b\u103c\u103d\u103e]+)", "\\1\\2\u1031"),

    # Reorder AI and medial WA
    ("\u1032\u103d", "\u103d\u1032"),

    # Reorder vowel I/II and medial YA
    ("([\u102d\u102e])\u103b", "\u103b\\1"),

    # Reorder medial WA and YA
    ("\u103d\u103b", "\u103b\u103d"),

    # Reorder asat and dot below
    ("\u103a\u1037", "\u1037\u103a"),

    # Remove duplicate U after vowel
    ("\u102f(\u102d|\u102e|\u1036|\u1037)\u102f", "\u102f\\1"),

    # Reorder U/UU and vowel I/II
    ("(\u102f|\u1030)(\u102d|\u102e)", "\\2\\1"),

    # Reorder medial HA and YA/RA
    ("(\u103e)(\u103b|\u103c)", "\\2\\1"),

    # U+1025 -> U+1009 before asat/AA
    ("\u1025(?=[\u1037]?[\u103a\u102c])", "\u1009"),

    # U+1025 + vowel II -> U+1026
    ("\u1025\u102e", "\u1026"),

    # CA + medial YA -> JHA
    ("\u1005\u103b", "\u1008"),

    # Reorder anusvara and U/UU
    ("\u1036(\u102f|\u1030)", "\\1\u1036"),

    # Reorder E + dot + medial HA
    ("\u1031\u1037\u103e", "\u103e\u1031\u1037"),

    # Reorder E + medial HA + AA
    ("\u1031\u103e\u102c", "\u103e\u1031\u102c"),

    # Tall AA + asat combination
    ("\u105a", "\u102b\u103a"),

    # Reorder E + medial YA + medial HA
    ("\u1031\u103b\u103e", "\u103b\u103e\u1031"),

    # Reorder vowel I/II and medial WA/HA
    ("(\u102d|\u102e)(\u103d|\u103e)", "\\2\\1"),

    # Reorder AA and stacked consonant
    ("\u102c\u1039([\u1000-\u1021])", "\u1039\\1\u102c"),

    # Complex reordering with medial RA + asat + stacked
    ("\u1039\u103c\u103a\u1039([\u1000-\u1021])", "\u103a\u1039\\1\u103c"),

    # Reorder medial RA and stacked consonant
    ("\u103c\u1039([\u1000-\u1021])", "\u1039\\1\u103c"),

    # Reorder anusvara and stacked consonant
    ("\u1036\u1039([\u1000-\u1021])", "\u1039\\1\u1036"),

    # Expand abbreviated form
    ("\u104e", "\u104e\u1004\u103a\u1038"),

    # Digit 0 + AA/AI -> WA + AA/AI
    ("\u1040(\u102b|\u102c|\u1036)", "\u101d\\1"),

    # U+1025 + asat -> U+1009 + asat
    ("\u1025\u1039", "\u1009\u1039"),

    # Reorder consonant + medial RA + E + medial WA
    ("([\u1000-\u1021])\u103c\u1031\u103d", "\\1\u103c\u103d\u1031"),

    # Reorder consonant + medial YA + E + medial WA + optional HA
    ("([\u1000-\u1021])\u103b\u1031\u103d(\u103e)?", "\\1\u103b\u103d\\2\u1031"),

    # Reorder consonant + medial WA + E + medial YA
    ("([\u1000-\u1021])\u103d\u1031\u103b", "\\1\u103b\u103d\u1031"),

    # Reorder consonant + E + stacked consonant
    ("([\u1000-\u1021])\u1031(\u1039[\u1000-\u1021]\u103d?)", "\\1\\2\u1031"),

    # Reorder visarga and asat
    ("\u1038\u103a", "\u103a\u1038"),

    # Remove redundant vowel I + asat combinations
    ("\u102d\u103a|\u103a\u102d", "\u102d"),

    # Remove asat after vowel I + U
    ("\u102d\u102f\u103a", "\u102d\u102f"),

    # Remove space before dot below
    ("\u0020\u1037", "\u1037"),

    # Reorder dot below and anusvara
    ("\u1037\u1036", "\u1036\u1037"),

    # Remove duplicate vowel I
    ("[\u102d]+", "\u102d"),

    # Remove duplicate asat
    ("[\u103a]+", "\u103a"),

    # Remove duplicate medial WA
    ("[\u103d]+", "\u103d"),

    # Remove duplicate dot below
    ("[\u1037]+", "\u1037"),

    # Remove duplicate vowel II
    ("[\u102e]+", "\u102e"),

    # Normalize vowel I + II -> II
    ("\u102d\u102e|\u102e\u102d", "\u102e"),

    # Reorder U + vowel I
    ("\u102f\u102d", "\u102d\u102f"),

    # Remove double dot below
    ("\u1037\u1037", "\u1037"),

    # Remove double AI
    ("\u1032\u1032", "\u1032"),

    # Digit 4 + NGA + asat + visarga -> abbreviated form
    ("\u1044\u1004\u103a\u1038", "\u104E\u1004\u103a\u1038"),

    # Reorder vowel I/II + stacked consonant
    ("([\u102d\u102e])\u1039([\u1000-\u1021])", "\u1039\\2\\1"),

    # Reorder medial RA + E + stacked consonant
    ("(\u103c\u1031)\u1039([\u1000-\u1021])", "\u1039\\2\\1"),

    # Reorder anusvara and medial WA
    ("\u1036\u103d", "\u103d\u1036"),

    # Digit 7 -> RA in certain contexts (final)
    ("\u1047((?=[\u1000-\u1021]\u103a)|(?=[\u102c-\u1030\u1032\u1036-\u1038\u103d\u103e]))", "\u101b"),
]
