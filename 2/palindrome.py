cat > task1/palindrome.py << 'EOF'
def is_palindrome(text: str) -> bool:
    """
    Проверяет, является ли строка палиндромом.
    
    Args:
        text (str): Входная строка для проверки
        
    Returns:
        bool: True если строка палиндром, иначе False
    """
    # Убираем пробелы и приводим к нижнему регистру
    cleaned_text = ''.join(text.lower().split())
    return cleaned_text == cleaned_text[::-1]


def test_palindrome() -> None:
    """Тестирование функции проверки палиндрома."""
    test_cases = [
        ("А роза упала на лапу Азора", True),
        ("hello", False),
        ("level", True),
        ("", True),
        ("мадам", True),
        ("казак", True),
        ("python", False),
    ]
    
    print("Тестирование функции is_palindrome:")
    print("=" * 40)
    
    for text, expected in test_cases:
        result = is_palindrome(text)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{text}' -> {result} (ожидалось: {expected})")


if __name__ == "__main__":
    test_palindrome()
EOF