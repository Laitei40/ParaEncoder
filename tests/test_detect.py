import para.detect as detect


def test_is_zawgyi_true():
    assert detect.is_zawgyi("\u106A\u1031\u1000") is True


def test_detect_unknown_on_ascii():
    assert detect.detect_encoding("hello") == "unknown"


ZAWGYI_FIXTURES = [
    "\u1031\u103B\u1000\u103A\u102C",  # prefixed E + medial order
    "\u1064\u102D\u1031\u1000",  # kinzi with i-vowel and E before base
]


UNICODE_FIXTURES = [
    "\u1019\u103C\u1014\u103A\u1038",  # မြန်မာ
    "\u1019\u103C\u1014\u103A\u1038\u1005\u102C",  # မြန်မာစာ
]


def test_detect_on_corpus_samples():
    for sample in ZAWGYI_FIXTURES:
        assert detect.detect_encoding(sample) == "zawgyi"
    for sample in UNICODE_FIXTURES:
        assert detect.detect_encoding(sample) == "unicode"


def test_detect_unknown_on_short_myanmar():
    assert detect.detect_encoding("\u1010\u1014") == "unknown"
