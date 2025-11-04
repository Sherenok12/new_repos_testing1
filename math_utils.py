def factorial(n):
    """Обчислює факторіал числа n."""
    if n < 0:
        raise ValueError("Факторіал не визначено для від’ємних чисел")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def average(numbers):
    """Обчислює середнє значення для списку чисел."""
    if not numbers:
        raise ValueError("Список порожній")
    return sum(numbers) / len(numbers)


def is_even(n):
    """Перевіряє, чи є число парним."""
    return n % 2 == 0


def max_difference(numbers):
    """Знаходить різницю між найбільшим і найменшим числом."""
    if not numbers:
        raise ValueError("Список порожній")
    return max(numbers) - min(numbers)


def normalize(numbers):
    """Повертає список, нормалізований до [0, 1]."""
    if not numbers:
        raise ValueError("Список порожній")
    min_val = min(numbers)
    max_val = max(numbers)
    if min_val == max_val:
        return [0.5 for _ in numbers]
    return [(x - min_val) / (max_val - min_val) for x in numbers]
