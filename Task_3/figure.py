from math import sqrt, pi


class Figure:
    def __init__(self, name: str):
        self.name = name

    def area_calculation(self):
        pass

    def perimeter_calculation(self):
        pass

    def comparison_area(self, other) -> str:
        if self.area_calculation() < other.area_calculation():
            return f"{self.name} меньше по площади чем {other.name.lower()}"
        elif self.area_calculation() > other.area_calculation():
            return f"{self.name} больше по площади чем {other.name.lower()}"
        else:
            return (f"{self.name} равны по площади "
                    f"с фигурой {other.name.lower()}")

    def comparison_perimeter(self, other) -> str:
        if self.perimeter_calculation() < other.perimeter_calculation():
            return f"{self.name} меньше по периметру чем {other.name.lower()}"
        elif self.perimeter_calculation() > other.perimeter_calculation():
            return f"{self.name} больше по площади чем {other.name.lower()}"
        else:
            return (f"{self.name} равны по периметру "
                    f"с фигурой {other.name.lower()}")


class Square(Figure):
    def __init__(self, name: str, size_side: float):
        super().__init__(name)
        self.size_side = size_side

    def area_calculation(self) -> float:
        return self.size_side ** 2

    def perimeter_calculation(self) -> float:
        return self.size_side * 4


class Triangle(Figure):
    def __init__(self, name: str, size_side1: float,
                 size_side2: float, size_side3: float):
        super().__init__(name)
        self.size_side1 = size_side1
        self.size_side2 = size_side2
        self.size_side3 = size_side3

    def area_calculation(self) -> float:
        p: float = (self.size_side1 + self.size_side2 + self.size_side3) / 2
        return sqrt(p * (p - self.size_side1) *
                    (p - self.size_side2) * (p - self.size_side3))

    def perimeter_calculation(self) -> float:
        return self.size_side1 + self.size_side2 + self.size_side3


class Rectangle(Figure):
    def __init__(self, name: str, size_side1: float, size_side2: float):
        super().__init__(name)
        self.size_side1 = size_side1
        self.size_side2 = size_side2

    def area_calculation(self) -> float:
        return self.size_side1 * self.size_side2

    def perimeter_calculation(self) -> float:
        return self.size_side1 * 2 + self.size_side2 * 2


class Circle(Figure):
    def __init__(self, name: str, radius: float):
        super().__init__(name)
        self.radius = radius

    def area_calculation(self) -> float:
        return pi * (self.radius ** 2)

    def perimeter_calculation(self) -> float:
        return 2 * pi * self.radius
