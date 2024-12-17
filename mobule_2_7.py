def generate_password(n):
    # Проверяем, что n находится в допустимом диапазоне
    if not (3 <= n <= 20):
        raise ValueError("n должно быть в диапазоне от 3 до 20")

    result = ""
    for a in range(1, n):
        b = n - a
        result += f"{a}{b}"

    return result


# Пример использования
n = int(input("Введите число n: "))
password = generate_password(n)
print(f"Пароль для числа {n}: {password}")
