def test_empty_string():
    from src.vowel_counter import count_vowels
    assert count_vowels("") == 0

def test_string_without_vowels():
    """Тест для строки без гласных"""
    from src.vowel_counter import count_vowels
    assert count_vowels("bcdfg") == 0
    assert count_vowels("xyz") == 0
    assert count_vowels("123!@#") == 0

def test_only_vowels():
    """Тест для строки только из гласных"""
    from src.vowel_counter import count_vowels
    assert count_vowels("aeiou") == 5
    assert count_vowels("aei") == 3

def test_mixed_case():
    """Тест для строки с разным регистром"""
    from src.vowel_counter import count_vowels
    assert count_vowels("Hello World") == 3
    assert count_vowels("AEIOU") == 5
    assert count_vowels("AaEeIiOoUu") == 10

def test_non_string_input():
    """Тест для нестроковых типов (TypeError)"""
    from src.vowel_counter import count_vowels
    
    # Проверяем, что функция вызывает TypeError для нестрок
    if not isinstance("test", str):
        print("ERROR: String check failed")
    
    # Проверяем числа
    try:
        count_vowels(123)
        print("ERROR: Should have raised TypeError for int")
        assert False
    except TypeError:
        pass
    
    # Проверяем float
    try:
        count_vowels(3.14)
        print("ERROR: Should have raised TypeError for float")
        assert False
    except TypeError:
        pass
    
    # Проверяем None
    try:
        count_vowels(None)
        print("ERROR: Should have raised TypeError for None")
        assert False
    except TypeError:
        pass
    
    # Проверяем список
    try:
        count_vowels(["a", "b", "c"])
        print("ERROR: Should have raised TypeError for list")
        assert False
    except TypeError:
        pass