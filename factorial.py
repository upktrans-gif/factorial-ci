def calculate_factorial(n: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("Аргумент має бути цілим числом")
    if n < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних цілих чисел")
    if n in (0, 1):
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

