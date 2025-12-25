def count_vowels(s):
    """Counts vowels in a string."""
    # Type check
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
if __name__ == "__main__":
    print("=" * 50)
    print("ИНТЕРАКТИВНЫЙ ПОДСЧЁТ ГЛАСНЫХ")
    print("=" * 50)
    print("Вводите строки для анализа.")
    print("Для выхода введите: стоп, stop, exit или пустую строку.")
    print("-" * 50)

    while True:
        user_input = input("\nВведите строку: ").strip()

        # Проверка команд выхода
        if not user_input or user_input.lower() in ['стоп', 'stop', 'exit']:
            print("Завершение работы. До свидания!")
            break

        try:
            result = count_vowels(user_input)
            print(f"✅ В строке '{user_input}' — {result} гласных.")
        except TypeError as e:
            print(f"❌ Ошибка: {e}")
        except Exception as e:
            print(f"❌ Неожиданная ошибка: {e}")