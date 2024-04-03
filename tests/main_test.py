import pytest

from main import count_words


@pytest.mark.parametrize(
    "text, expected_words",
    [
        ("Це тестовий текст, який має кілька слів.", 7),
        ("Це тестове речення!", 3),
        ("", 0),
    ],
)
def test_count_words(text, expected_words):
    num_of_words = count_words(text)
    assert num_of_words == expected_words
