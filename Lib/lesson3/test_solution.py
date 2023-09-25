# Напишите тесты для функции without(coll, *values).
# Эта функция должна принимать список в качестве первого параметра,
# а затем возвращать его копию, из которой исключены значения,
# переданные вторым и последующими параметрами.
# Если список содержит несколько одинаковых исключаемых элементов, то исключаются они все:
#
# from functions import get_function
# without = get_function()
#
# without([2, 1, 2, 3, 4], 2, 3)  # [1, 4]
# without([], 2)  # []


from functions import get_function

without = get_function()


# BEGIN (write your solution here)

def test_function():
    assert without([2, 1, 2, 3, 4], 2, 3) == [1, 4]


def test_function2():
    assert without([], 2) == []

# END
