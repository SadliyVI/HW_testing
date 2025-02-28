import pytest
from  task_1_2 import vote

# Параметризованный тест для основного случая
@pytest.mark.parametrize('votes_input, expected_output', [
    ([1, 1, 1 ,2 ,3], 1),
    ([1 ,2 ,3 ,2 ,2], 2)
])
def test_vote_basic(votes_input , expected_output): # Победитель единственный
    assert vote(votes_input) == expected_output

def test_one_element(): # Один элемент в списке
    assert vote([5]) == 5

def test_all_items_equal():  # Все элементы одинаковые
    assert vote([4 ,4 ,4]) == 4

def test_not_integer(): # Элементы списка не цифры
    with pytest.raises(ValueError):
        vote(['a', 5, 'b'])

# Тест для пустого списка (ожидается ошибка)
@pytest.mark.xfail(reason='Ожидается ошибка для пустого списка')
def test_empty_list():
    with pytest.raises(ValueError):
        vote([])

# Пропускаем тест для отрицательных значений (как пример)
@pytest.mark.skipif(True , reason='Модуль проверяющий на отрицательные '
                                  'значения еще не готов')
def test_negative_values():
    assert vote([-1 ,-1 ,-2]) == -1

# Тест на обработку ничьей заведомо провальный, так как в функции не
# проработан случай если ожидается два одинаковых значения
@pytest.mark.xfail(reason='Возвращает первый элемент при ничьей')
def test_draw_case():
    assert vote([10 ,20 ,20 ,10]) == 10
