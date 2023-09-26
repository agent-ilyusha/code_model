from main import detective
import pytest

test_list = [('0', '8'), ('52', '22 42 82 62 51 55 53'),
             ('88', '58 78 08 98 85 87 80 89'), ('1', '4 2'),
             ('4', '7 5 1'), ('7', ' 8 4'), ('3', '6 2'), ('6', '9 5 3'), ('9', ' 8 6')]


@pytest.mark.parametrize("test_input,expected", test_list)
def test_func(test_input, expected):
    assert ' '.join(detective(test_input)) == expected

