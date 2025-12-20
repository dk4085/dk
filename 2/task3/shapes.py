
import math
from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar('T', bound='Shape')


class Shape(ABC):
    """Абстрактный базовый класс для геометрических фигур."""
    
    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры."""
        pass
    
    @abstractmethod
    def perimeter(self) -> float:
        """Вычисляет периметр фигуры."""
        pass
    
    def area_greater_than(self, other: T) -> bool:
        """Сравнивает площадь с другой фигурой."""
        return self.area() > other.area()
    
    def area_less_than(self, other: T) -> bool:
        """Сравнивает площадь с другой фигурой."""
        return self.area() < other.area()
    
    def perimeter_greater_than(self, other: T) -> bool:
        """Сравнивает периметр с другой фигурой."""
        return self.perimeter() > other.perimeter()
    
    def perimeter_less_than(self, other: T) -> bool:
        """Сравнивает периметр с другой фигурой."""
        return self.perimeter() < other.perimeter()


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"


class Square(Shape):
    def __init__(self, side: float) -> None:
        if side <= 0:
            raise ValueError("Сторона должна быть положительным числом")
        self.side = side
    
    def area(self) -> float:
        return self.side ** 2
    
    def perimeter(self) -> float:
        return 4 * self.side
    
    def __repr__(self) -> str:
        return f"Square(side={self.side})"


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        if width <= 0 or height <= 0:
            raise ValueError("Стороны должны быть положительными числами")
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float) -> None:
        sides = [a, b, c]
        if any(s <= 0 for s in sides):
            raise ValueError("Все стороны должны быть положительными числами")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("Треугольник с такими сторонами не существует")
        self.a = a
        self.b = b
        self.c = c
    
    def area(self) -> float:
        # Формула Герона
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c
    
    def __repr__(self) -> str:
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


def test_shapes() -> None:
    """Тестирование классов фигур."""
    shapes = [
        Circle(5),
        Square(4),
        Rectangle(3, 6),
        Triangle(3, 4, 5)
    ]
    
    for shape in shapes:
        print(f"{shape}:")
        print(f"  Площадь: {shape.area():.2f}")
        print(f"  Периметр: {shape.perimeter():.2f}")
    
    # Сравнение
    circle = Circle(5)
    square = Square(4)
    print(f"\nПлощадь круга больше площади квадрата: {circle.area_greater_than(square)}")


if __name__ == "__main__":
    test_shapes()
