from math_utils import factorial, average, is_even, max_difference, normalize


def main():
    numbers_mas = [2, 4, 6]
    print("Список чисел:", numbers_mas)

    print("Середнє значення:", average(numbers_mas))
    print("Факторіал першого числа:", factorial(numbers_mas[0]))
    print("Чи перше число парне?:", is_even(numbers_mas[0]))
    print("Різниця між max і min:", max_difference(numbers_mas))
    print("Нормалізовані значення:", normalize(numbers_mas))

    try:
        factorial(-3)
    except ValueError as e:
        print("Помилка:", e)


if __name__ == "__main__":
    main()
