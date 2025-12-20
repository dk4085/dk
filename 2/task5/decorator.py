
import time
from typing import Callable, Any
from functools import wraps


def timing_decorator(func: Callable) -> Callable:
    """
    Декоратор, который выводит время выполнения функции.
    
    Args:
        func: Функция для декорирования
        
    Returns:
        Обернутая функция с измерением времени
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.6f} секунд")
        return result
    return wrapper


# Пример 1: Функция сложения
@timing_decorator
def add_numbers(a: int, b: int) -> int:
    """Складывает два числа и выводит результат."""
    result = a + b
    print(f"Результат сложения: {result}")
    return result


# Пример 2: Функция работы с файлами
@timing_decorator
def process_file(input_file: str = "input.txt", output_file: str = "output.txt") -> None:
    """
    Читает два числа из файла, складывает их и записывает результат.
    
    Args:
        input_file: Имя входного файла
        output_file: Имя выходного файла
    """
    try:
        with open(input_file, 'r') as f:
            numbers = f.read().strip().split()
            if len(numbers) < 2:
                raise ValueError("Файл должен содержать как минимум два числа")
            a, b = map(float, numbers[:2])
    except FileNotFoundError:
        print(f"Файл {input_file} не найден")
        return
    
    result = a + b
    
    with open(output_file, 'w') as f:
        f.write(str(result))
    
    print(f"Результат {a} + {b} = {result} записан в {output_file}")


def create_test_files() -> None:
    """Создает тестовые файлы, если они не существуют."""
    import os
    if not os.path.exists("input.txt"):
        with open("input.txt", "w") as f:
            f.write("10 20")


def test_decorator() -> None:
    """Тестирование декоратора."""
    print("Тест 1 - Сложение чисел:")
    add_numbers(5, 3)
    
    print("\nТест 2 - Обработка файлов:")
    create_test_files()
    process_file()


if __name__ == "__main__":
    test_decorator()
