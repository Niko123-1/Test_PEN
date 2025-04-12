import pytest
from pen import Pen # импортируем класс Pen из pen.py


@pytest.fixture
def pen():
    """
       Фикстура для создания объекта Pen с начальным количеством чернил = 10,
       размером буквы = 1.0 и цветом 'green'.
       Для тестов, где не требуется изменение этих параметров.
    """
    return Pen(ink_container_value=10, size_letter=1.0, color='green')


# проверка метода инициализации
def test_initialization(pen):
   assert pen.ink_container_value == 10
   assert pen.size_letter == 1.0
   assert pen.color == 'green'


# проверка метода получения цвета
def test_get_color(pen):
   assert pen.get_color() == pen.color


# проверка наличия чернил
def test_check_ink_presence(pen):
   assert pen.check_pen_state()


# проверка отсутствия чернил
def test_check_ink_absence(pen):
   pen.ink_container_value = 0
   assert not pen.check_pen_state()


# проверка метода печати цвета чернил
def test_do_something_else(pen, capsys):
   pen.do_something_else()
   captured = capsys.readouterr()
   assert captured.out.strip() == "green"


# проверка написания с нулевым кол-вом чернил
def test_check_zero_ink(pen):
   pen.ink_container_value = 0
   assert pen.write('Hello') == ''
   assert pen.ink_container_value == 0


# проверка написания с кол-вом чернил большим размера слова
def test_write_with_sufficient_ink(pen):
   result = pen.write('h')
   assert result == 'h'
   assert pen.ink_container_value == 9


# проверка написания с кол-вом чернил совпадающим с размером слова
def test_write_with_exact_ink(pen):
   result = pen.write('helloworld')
   assert result == 'helloworld'
   assert pen.ink_container_value == 0


# проверка написания с кол-вом чернил меньше чем размер слова
def test_write_with_insufficient_ink(pen):
   pen.size_letter = 3.0
   result = pen.write('hello')
   assert result == 'hel'
   assert pen.ink_container_value == 1


# проверка написания с кол-вом чернил меньше чем размер буквы
def test_write_with_insufficient_ink_size_letter_more_than_ink(pen):
   pen.size_letter = 17.0
   result = pen.write('hello')
   assert result == ''
   assert pen.ink_container_value == 10


# проверка написания с дробным размером буквы
def test_write_with_fractional_size_letter(pen):
   pen.size_letter = 0.5
   result = pen.write("hello")
   assert result == "hello"
   assert pen.ink_container_value == 7.5


# проверка написания с размером буквы 0
def test_write_with_size_letter_zero(pen):
   pen.size_letter = 0
   result = pen.write('hello')
   assert result == ''
   assert pen.ink_container_value == 10


# проверка написания пустого слова
def test_write_empty_word(pen):
   result = pen.write('')
   assert result == ''
   assert pen.ink_container_value == 10


# проверка на отрицательное кол-во чернил
def test_negative_ink_container_value(pen):
   pen.ink_container_value = -10
   assert pen.write("hello") == ""


# проверка на отрицательное значение размера буквы
def test_negative_size_letter(pen):
   pen.size_letter = -3
   assert pen.write("hello") == ""
   assert pen.ink_container_value == 10