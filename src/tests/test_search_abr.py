import pytest
from search_abr import CursAbrIter


def test_create_new_object():
    abrs = CursAbrIter(['aaa', 'aab', 'bbb', 'bbc'])
    assert abrs.data == ['aaa', 'aab', 'bbb', 'bbc']


def test_raise_value_error_exception_if_start_data_is_fail_one():
    with pytest.raises(ValueError, match='Неверные входные данные'):
        CursAbrIter('zzz')


def test_raise_value_error_exception_if_start_data_is_fail_two():
    with pytest.raises(ValueError, match='Неверные входные данные'):
        CursAbrIter([])


def test_raise_value_error_exception_if_start_data_is_fail_tree():
    with pytest.raises(ValueError, match='Неверные входные данные'):
        CursAbrIter([1, 2])


def test_add_new_data_part_1():
    abrs = CursAbrIter(['aaa', 'aab', 'bbb', 'bbc'])
    abrs.add_new_abr('ccc')
    assert abrs.data == ['aaa', 'aab', 'bbb', 'bbc', 'ccc']


def test_add_new_data_part_2():
    abrs = CursAbrIter(['aaa', 'aab', 'bbb', 'bbc'])
    abrs.add_new_abr(['ccc', 'ddd'])
    assert abrs.data == ['aaa', 'aab', 'bbb', 'bbc', 'ccc', 'ddd']


def test_raise_value_error_when_validate_adding_data_part_1():
    with pytest.raises(ValueError, match='Должно передаваться AddAbr'):
        abrs = CursAbrIter(['aaa', 'aab', 'bbb', 'bbc'])
        abrs.add_new_abr(('ccc', 'ddd'))


def test_raise_value_error_when_validate_adding_data_part_2():
    with pytest.raises(ValueError, match='В списке должны быть строки'):
        abrs = CursAbrIter(['aaa', 'aab', 'bbb', 'bbc'])
        abrs.add_new_abr([1, 'ddd'])


def test_setter_new_data_part1():
    abrs = CursAbrIter(['aaa', 'aab', 'bbb', 'bbc'])
    abrs.data = ['uuu']
    assert abrs.data == ['uuu']


def test_setter_new_data_part2():
    abrs = CursAbrIter(['aaa', 'aab', 'bbb', 'bbc'])
    abrs.data = []
    assert abrs.data == ['aaa', 'aab', 'bbb', 'bbc']


def test_setter_new_data_part3():
    abrs = CursAbrIter(['aaa', 'aab', 'bbb', 'bbc'])
    abrs.data = ('uuu',)
    assert abrs.data == ['aaa', 'aab', 'bbb', 'bbc']


def test_setter_new_data_part4():
    abrs = CursAbrIter(['aaa', 'aab', 'bbb', 'bbc'])
    abrs.data = ['uuu', 7]
    assert abrs.data == ['aaa', 'aab', 'bbb', 'bbc']


if __name__ == "__main__":
    test_create_new_object()
    test_raise_value_error_exception_if_start_data_is_fail_one()
    test_raise_value_error_exception_if_start_data_is_fail_two()
    test_raise_value_error_exception_if_start_data_is_fail_tree()
    test_add_new_data_part_1()
    test_add_new_data_part_2()
    test_raise_value_error_when_validate_adding_data_part_1()
    test_raise_value_error_when_validate_adding_data_part_2()
    test_setter_new_data_part1()
    test_setter_new_data_part2()
    test_setter_new_data_part3()
    test_setter_new_data_part4()
    print('Тесты успешно пройдены')
