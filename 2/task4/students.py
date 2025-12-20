
from typing import Optional


class Person:
    """Базовый класс для человека."""
    
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    @property
    def full_name(self) -> str:
        """Возвращает полное имя."""
        return f"{self.first_name} {self.last_name}"
    
    def print_info(self) -> None:
        """Выводит информацию о человеке."""
        print(f"ФИО: {self.full_name}")
        print(f"Возраст: {self.age}")


class Student(Person):
    def __init__(self, first_name: str, last_name: str, age: int,
                 group_number: str, average_score: float) -> None:
        super().__init__(first_name, last_name, age)
        self.group_number = group_number
        self.average_score = average_score
    
    def calculate_scholarship(self) -> int:
        """Вычисляет размер стипендии для студента."""
        if self.average_score == 5:
            return 6000
        elif 4 <= self.average_score < 5:
            return 4000
        return 0
    
    def print_scholarship(self) -> None:
        """Выводит размер стипендии."""
        scholarship = self.calculate_scholarship()
        print(f"Стипендия: {scholarship}р")
    
    def scholarship_greater_than(self, other: 'Student') -> bool:
        """Сравнивает стипендию с другим студентом/аспирантом."""
        return self.calculate_scholarship() > other.calculate_scholarship()
    
    def scholarship_less_than(self, other: 'Student') -> bool:
        """Сравнивает стипендию с другим студентом/аспирантом."""
        return self.calculate_scholarship() < other.calculate_scholarship()


class GraduateStudent(Student):
    def __init__(self, first_name: str, last_name: str, age: int,
                 group_number: str, average_score: float,
                 research_title: str) -> None:
        super().__init__(first_name, last_name, age, group_number, average_score)
        self.research_title = research_title
    
    def calculate_scholarship(self) -> int:
        """Вычисляет размер стипендии для аспиранта."""
        if self.average_score == 5:
            return 8000
        elif 4 <= self.average_score < 5:
            return 6000
        return 0
    
    def print_info(self) -> None:
        """Выводит информацию об аспиранте."""
        super().print_info()
        print(f"Научная работа: {self.research_title}")


def test_students() -> None:
    """Тестирование классов студентов."""
    student = Student("Иван", "Иванов", 20, "ГР-101", 4.8)
    graduate = GraduateStudent("Петр", "Петров", 25, "АСП-201", 5.0,
                               "Исследование алгоритмов")
    
    print("Студент:")
    student.print_info()
    student.print_scholarship()
    
    print("\nАспирант:")
    graduate.print_info()
    graduate.print_scholarship()
    
    print(f"\nСтипендия аспиранта больше студента: "
          f"{graduate.scholarship_greater_than(student)}")


if __name__ == "__main__":
    test_students()
