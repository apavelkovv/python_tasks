from figure import Square, Rectangle, Triangle, Circle


square1 = Square("Квадратик", 4)
rectangle1 = Rectangle("Прямоугольничек", 3, 6)
triangle1 = Triangle("Треугольничек", 3, 4, 5)
circle1 = Circle("Кружочек", 5)

print("Площади:")
print(f"{square1.name}: {square1.area_calculation()}")
print(f"{rectangle1.name}: {rectangle1.area_calculation()}")
print(f"{triangle1.name}: {triangle1.area_calculation()}")
print(f"{circle1.name}: {circle1.area_calculation()}")

print("\nПериметры:")
print(f"{square1.name}: {square1.perimeter_calculation()}")
print(f"{rectangle1.name}: {rectangle1.perimeter_calculation()}")
print(f"{triangle1.name}: {triangle1.perimeter_calculation()}")
print(f"{circle1.name}: {circle1.perimeter_calculation()}")

print("\nСравнение площадей:")
print(square1.comparison_area(rectangle1))
print(circle1.comparison_area(triangle1))
print(rectangle1.comparison_area(circle1))

print("\nСравнение периметров:")
print(square1.comparison_perimeter(rectangle1))
print(circle1.comparison_perimeter(triangle1))
print(rectangle1.comparison_perimeter(square1))
