
from math import sqrt


def add_numbers(number_one, number_two) -> int:
    sum_number: int = number_one + number_two
    return sum_number


def calculate_square_root(number):
    return sqrt(number)


def calc(your_number):
    if your_number <= 0:
        return None
    sqrt_num = calculate_square_root(your_number)
    srt_num = (
        'Мы вычислили квадратный корень из введённого вами числа. '
        'Это будет: ')
    return f'{srt_num}{sqrt_num}'


first_number = 10
second_number = 5

print('Сумма чисел: ', add_numbers(first_number, second_number))

print(calc(25.5))
