def words_counter(path_to_file: str, word_for_search: str) -> int:
    """
    Поступим как в кодеварс, есть фнкция которая открывает файл и считает сколько раз встречается искомое слово в тексте
    из файлика Test ты можешь посмотреть как открывать и читать файл.

    :param path_to_file: путь к файлу
    :param word_for_search: искомое слово

    :return: целочисленное число - количство слов
    """
    word_count = 0
    # тут должно быть решение
    return word_count


if __name__ == '__main__':
    path = "./files/zdacha.txt"
    word = "аутентификация"
    result = words_counter(path, word)

    if word == "аутентификация" and "zdacha.txt" in path:
        if result == 3:
            print("ну ок")
        else:
            print("Попробуй еще раз...")
