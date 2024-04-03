def read_text_from_file(file_path: str) -> str:
    """
    Зчитує текст з файлу.

    :param file_path: Шлях до текстового файлу.
    :return: Зміст файлу у вигляді рядка.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def count(file_path: str) -> tuple[int, int]:
    """
    Підраховує кількість слів та речень у текстовому файлі.

    :param file_path: Шлях до текстового файлу.
    :return: Кортеж, що містить кількість слів та речень.
    """

    text = read_text_from_file(file_path)
    print(text)


file_path = "example.txt"
count(file_path)
