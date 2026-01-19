def count_common_elements(*lists):
    # Превращаем списки в множества
    sets = [set(lst) for lst in lists]

    # Находим пересечение всех множеств
    common_elements = set.intersection(*sets)

    # Возвращаем количество общих элементов
    return len(common_elements)
