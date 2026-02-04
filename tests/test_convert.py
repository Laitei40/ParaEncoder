from para.convert import zg_to_unicode


def test_simple_replacement():
    zg = "\u106A\u1033"  # NGA in Zawgyi + tall AA
    expected = "\u1009\u102F"
    assert zg_to_unicode(zg, force=True, normalize=False) == expected


def test_normalization_runs():
    zg = "\u1031\u1000\u103C"  # Zawgyi-ordered E vowel
    converted = zg_to_unicode(zg, force=True, normalize=True)
    assert "\u1031" in converted and "\u1000" in converted


def test_kinzi_basic_conversion():
    zg = "\u1064\u1031\u1000"
    converted = zg_to_unicode(zg, force=True, normalize=True)
    assert "\u1004\u103A\u1039" in converted
    assert "\u1000" in converted


def test_kinzi_with_vowel_marker():
    zg = "\u108B\u1000"
    converted = zg_to_unicode(zg, force=True, normalize=True)
    assert "\u1004\u103A\u1039" in converted
    assert "\u102D" in converted


def test_tall_aa_mapping():
    zg = "\u1034"
    assert zg_to_unicode(zg, force=True, normalize=False) == "\u1030"


def test_asat_dot_swap():
    zg = "\u103A\u1037"
    assert zg_to_unicode(zg, force=True, normalize=False) == "\u1037\u103A"


def test_tall_u_dot_reorder():
    zg = "\u1036\u102F"
    assert zg_to_unicode(zg, force=True, normalize=False) == "\u102F\u1036"


def test_prefix_e_reorder_with_medial():
    zg = "\u1031\u103B\u1000"  # E vowel before YA medial
    converted = zg_to_unicode(zg, force=True, normalize=False)
    assert converted.startswith("\u103B\u1031")


def test_stacked_consonant_ka():
    zg = "\u1060\u1000"  # stacked KA + base KA
    converted = zg_to_unicode(zg, force=True, normalize=False)
    assert converted.startswith("\u1039\u1000")
