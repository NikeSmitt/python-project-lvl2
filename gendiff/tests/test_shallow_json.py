from gendiff.scripts.gendiff import generate_diff

PLUS = "  + "
MINUS = "  - "
EMPTY = "    "


def test_empty_files():
    FILE1 = 'gendiff/tests/fixtures/empty_1.json'
    FILE2 = 'gendiff/tests/fixtures/empty_2.json'

    assert generate_diff(FILE1, FILE2) == ''


def test_same_files():
    FILE = 'gendiff/tests/fixtures/file_1.json'
    OUTPUT = """{
    follow: False
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""

    assert generate_diff(FILE, FILE) == OUTPUT


def test_total_different_files():
    FILE1 = 'gendiff/tests/fixtures/file_1.json'
    FILE2 = 'gendiff/tests/fixtures/file_2.json'
    OUTPUT = ["{",
              f"{PLUS}Abbrev: ISO 8879:1986",
              f"{PLUS}Acronym: SGML",
              f"{MINUS}follow: False",
              f"{MINUS}host: hexlet.io",
              f"{MINUS}proxy: 123.234.53.22",
              f"{MINUS}timeout: 50",
              "}"
              ]
    assert "\n".join(OUTPUT) == generate_diff(FILE1, FILE2)


def test_different_files_with_same_keys():
    FILE1 = 'gendiff/tests/fixtures/file_2.json'
    FILE2 = 'gendiff/tests/fixtures/file_3.json'

    OUTPUT = ["{",
              f"{MINUS}Abbrev: ISO 8879:1986",
              f"{PLUS}Abbrev: ISO 8879:2021",
              f"{EMPTY}Acronym: SGML",
              f"{PLUS}follow: False",
              f"{PLUS}proxy: 123.234.53.22",
              "}"
              ]
    assert "\n".join(OUTPUT) == generate_diff(FILE1, FILE2)