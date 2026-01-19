from lab import count_common_elements


def test_count_common_elements():
    # Тест 1
    assert count_common_elements([1, 2, 3], [3, 4, 5], [3, 6, 7]) == 1, "Тест 1 провален"

    # Тест 2
    assert count_common_elements([1, 2, 3, 4], [3, 4, 5, 6], [4, 5, 6, 7]) == 1, "Тест 2 провален"

    # Тест 3
    assert count_common_elements([1, 2], [3, 4], [5, 6]) == 0, "Тест 3 провален"

    # Тест 4
    assert count_common_elements([1, 2, 3], [2, 3, 4], [3, 4, 5]) == 1, "Тест 4 провален"

    # Тест 5 (тест на пустые списки)
    assert count_common_elements([]) == 0, "Тест 5 провален"

    # Тест 6 (тест на несколько одинаковых элементов)
    assert count_common_elements([1, 1, 1], [1, 1, 1], [1, 1, 1]) == 1, "Тест 6 провален"

    print("Все тесты пройдены!")


# Запускаем тесты
if __name__ == "__main__":
    test_count_common_elements()
