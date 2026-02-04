from para.convert import zg_to_unicode


def test_unicode_mingalaba_is_preserved():
    """Unicode input must NEVER be modified by zg_to_unicode (contract guarantee)."""
    assert zg_to_unicode("မင်္ဂလာပါ") == "မင်္ဂလာပါ"


def test_zawgyi_myanmarjpyay_conversion():
    """Full Zawgyi sentence 'I love Myanmar' converts correctly."""
    zg = "ျမန္မာျပည္ကိုခ်စ္တယ္"
    expected = "မြန်မာပြည်ကိုချစ်တယ်"
    assert zg_to_unicode(zg, force=True) == expected


def test_simple_replacement():
    """Basic NGA + tall AA conversion."""
    zg = "\u106A\u1033"  # NGA variant + tall AA
    expected = "\u1009\u102F"  # NGA + U
    assert zg_to_unicode(zg, force=True) == expected


def test_kinzi_basic_conversion():
    """Kinzi character converts to NGA + asat + virama sequence."""
    # Kinzi typically appears with a consonant, e.g., ကၤ -> ကင်္
    zg = "\u1000\u1064"  # KA + kinzi
    converted = zg_to_unicode(zg, force=True)
    assert "\u1004\u103a\u1039" in converted


def test_kinzi_with_vowel_i():
    """Kinzi with vowel I marker."""
    # Kinzi+I typically appears with a consonant
    zg = "\u1000\u108b"  # KA + kinzi+I
    converted = zg_to_unicode(zg, force=True)
    assert "\u1004\u103a\u1039" in converted
    assert "\u102d" in converted


def test_tall_aa_mapping():
    """Tall AA (U+1033) -> U+102F."""
    zg = "\u1033"
    assert zg_to_unicode(zg, force=True) == "\u102F"


def test_tall_uu_mapping():
    """Tall UU (U+1034) -> U+1030."""
    zg = "\u1034"
    assert zg_to_unicode(zg, force=True) == "\u1030"


def test_stacked_consonant_ka():
    """Stacked KA (U+1060) -> virama + KA."""
    zg = "\u1060"
    assert zg_to_unicode(zg, force=True) == "\u1039\u1000"


def test_stacked_consonant_kha():
    """Stacked KHA (U+1061) -> virama + KHA."""
    zg = "\u1061"
    assert zg_to_unicode(zg, force=True) == "\u1039\u1001"


def test_stacked_consonant_ga():
    """Stacked GA (U+1062) -> virama + GA."""
    zg = "\u1062"
    assert zg_to_unicode(zg, force=True) == "\u1039\u1002"


def test_stacked_consonant_gha():
    """Stacked GHA (U+1063) -> virama + GHA."""
    zg = "\u1063"
    assert zg_to_unicode(zg, force=True) == "\u1039\u1003"


def test_stacked_consonant_ca():
    """Stacked CA (U+1065) -> virama + CA."""
    zg = "\u1065"
    assert zg_to_unicode(zg, force=True) == "\u1039\u1005"


def test_stacked_consonant_ja():
    """Stacked JA (U+1068) -> virama + JA."""
    zg = "\u1068"
    assert zg_to_unicode(zg, force=True) == "\u1039\u1007"


def test_stacked_consonant_ta():
    """Stacked TA variants (U+1071/U+1072) -> virama + TA."""
    assert zg_to_unicode("\u1071", force=True) == "\u1039\u1010"
    assert zg_to_unicode("\u1072", force=True) == "\u1039\u1010"


def test_stacked_consonant_tha():
    """Stacked THA variants (U+1073/U+1074) -> virama + THA."""
    assert zg_to_unicode("\u1073", force=True) == "\u1039\u1011"
    assert zg_to_unicode("\u1074", force=True) == "\u1039\u1011"


def test_stacked_consonant_pa():
    """Stacked PA (U+1078) -> virama + PA."""
    zg = "\u1078"
    assert zg_to_unicode(zg, force=True) == "\u1039\u1015"


def test_stacked_consonant_ma():
    """Stacked MA (U+107C) -> virama + MA."""
    zg = "\u107C"
    assert zg_to_unicode(zg, force=True) == "\u1039\u1019"


def test_stacked_consonant_la():
    """Stacked LA (U+1085) -> virama + LA."""
    zg = "\u1085"
    assert zg_to_unicode(zg, force=True) == "\u1039\u101C"


def test_medial_ya_conversion():
    """Medial YA variant (U+103A in Zawgyi) -> U+103B."""
    # After asat conversion, U+1039 becomes U+103A (asat)
    # Then U+103A becomes U+103B (medial YA)
    zg = "\u103a"  # Zawgyi medial YA
    converted = zg_to_unicode(zg, force=True)
    assert converted == "\u103b"


def test_medial_ra_conversion():
    """Medial RA variants -> U+103C."""
    # U+103B in Zawgyi is medial RA
    zg = "\u103b"
    converted = zg_to_unicode(zg, force=True)
    assert converted == "\u103c"


def test_medial_wa_conversion():
    """Medial WA (U+103C in Zawgyi) -> U+103D."""
    zg = "\u103c"
    converted = zg_to_unicode(zg, force=True)
    assert converted == "\u103d"


def test_medial_ha_conversion():
    """Medial HA (U+103D in Zawgyi) -> U+103E."""
    zg = "\u103d"
    converted = zg_to_unicode(zg, force=True)
    assert converted == "\u103e"


def test_asat_conversion():
    """Asat/virama (U+1039 in Zawgyi) -> U+103A."""
    zg = "\u1039"
    converted = zg_to_unicode(zg, force=True)
    assert converted == "\u103a"


def test_dot_below_variants():
    """Dot below variants (U+1094/U+1095) -> U+1037."""
    assert zg_to_unicode("\u1094", force=True) == "\u1037"
    assert zg_to_unicode("\u1095", force=True) == "\u1037"


def test_na_variant():
    """NA variant (U+108F) -> U+1014."""
    zg = "\u108F"
    assert zg_to_unicode(zg, force=True) == "\u1014"


def test_ra_variant():
    """RA variant (U+1090) -> U+101B."""
    zg = "\u1090"
    assert zg_to_unicode(zg, force=True) == "\u101B"


def test_nga_variant():
    """NGA variant (U+106A) -> U+1009."""
    zg = "\u106A"
    assert zg_to_unicode(zg, force=True) == "\u1009"


def test_great_sa():
    """Great SA (U+1086) -> U+103F."""
    zg = "\u1086"
    assert zg_to_unicode(zg, force=True) == "\u103F"


def test_tall_aa_asat():
    """Tall AA + asat combination (U+105A) -> U+102B U+103A."""
    zg = "\u105A"
    assert zg_to_unicode(zg, force=True) == "\u102B\u103A"


def test_empty_string():
    """Empty string returns empty."""
    assert zg_to_unicode("") == ""


def test_ascii_passthrough():
    """ASCII text passes through unchanged."""
    assert zg_to_unicode("hello world", force=True) == "hello world"

