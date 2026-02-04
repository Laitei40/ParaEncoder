from para.normalize import normalize_unicode


def test_unicode_mingalaba_normalization_is_noop():
    """normalize_unicode must NEVER modify valid Unicode (contract guarantee)."""
    assert normalize_unicode("မင်္ဂလာပါ") == "မင်္ဂလာပါ"


def test_empty_string():
    assert normalize_unicode("") == ""


def test_ascii_passthrough():
    assert normalize_unicode("hello") == "hello"
