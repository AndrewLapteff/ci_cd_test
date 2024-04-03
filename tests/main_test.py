import pytest

from main import count_sentences, count_words


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


@pytest.mark.parametrize(
    "text, expected_sentences",
    [("Перше речення. Друге речення! Третє речення?", 3), ("", 0)],
)
def test_count_sentences(text, expected_sentences):
    num_sentences = count_sentences(text)
    assert num_sentences == expected_sentences
