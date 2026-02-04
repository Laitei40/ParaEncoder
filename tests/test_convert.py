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
