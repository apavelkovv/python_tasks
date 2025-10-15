from students import Student, Aspirant

student1 = Student("Железников", "Клим", "Алексеевич", 19, "5132704/30801", 5)
student2 = Student("Фошкин", "Павел", "Дмитриевич", 20, "5132704/30801", 4.3)
aspirant1 = Aspirant("Павелков", "Артём",
                     "Владимирович", 25, "5132704/30801",
                     5, "Исследование человека-паука на полезность обществу")
aspirant2 = Aspirant("Козлов", "Дмитрий",
                     "Николаевич", 26, "5132704/30801",
                     4.5, "Моделирование полезности и комфортности котиков")

print("Информация о людях:")
print(student1.info_person())
print(aspirant1.info_person())

print("\nСтипендии:")
print(f"{student1.surname} получает {student1.scholarship()} руб.")
print(f"{student2.surname} получает {student2.scholarship()} руб.")
print(f"{aspirant1.surname} получает {aspirant1.scholarship()} руб.")
print(f"{aspirant2.surname} получает {aspirant2.scholarship()} руб.")

print("\nСравнение стипендий:")
print(student1.comparison_scholarship(student2))
print(student2.comparison_scholarship(aspirant2))
print(aspirant1.comparison_scholarship(aspirant2))
print(student2.comparison_scholarship(aspirant1))
