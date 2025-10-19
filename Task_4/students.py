class Student:

    excellent_scholarship: int = 6000
    normal_scholarship: int = 4000

    def __init__(self, surname: str, name: str, middle_name: str,
                 age: int, group_number: str, grade_point_average: float):
        self.name = name
        self.middle_name = middle_name
        self.surname = surname
        self.age = age
        self.group_number = group_number
        self.grade_point_average = grade_point_average

    def info_person(self) -> str:
        return (f'Ваше ФИО: {self.surname} {self.name} {self.middle_name}.'
                f' Ваш возраст: {self.age}')

    def scholarship(self) -> int:
        if self.grade_point_average == 5:
            return self.excellent_scholarship
        elif 4 <= self.grade_point_average < 5:
            return self.normal_scholarship
        else:
            return 0

    def comparison_scholarship(self, other) -> str:
        scholarship1 = self.scholarship()
        scholarship2 = other.scholarship()
        if scholarship1 > scholarship2:
            return (f'{self.surname} {self.name} {self.middle_name} '
                    f'имеет большую стипендию чем '
                    f'{other.surname} {other.name} {other.middle_name} на '
                    f'{scholarship1 - scholarship2} рублей.')
        elif scholarship1 < scholarship2:
            return (f'{other.surname} {other.name} {other.middle_name} '
                    f'имеет большую стипендию чем '
                    f'{self.surname} {self.name} {self.middle_name} на '
                    f'{scholarship2 - scholarship1} рублей.')
        else:
            return (f'{self.surname} {self.name} {self.middle_name} и '
                    f'{other.surname} {other.name} {other.middle_name} '
                    f'имеют равную стипендию и '
                    f'она составляет {scholarship1}')


class Aspirant(Student):

    excellent_scholarship: int = 8000
    normal_scholarship: int = 6000

    def __init__(self, surname: str, name: str, middle_name: str,
                 age: int, group_number: str, grade_point_average: float,
                 science_work: str):
        super().__init__(surname, name, middle_name, age,
                         group_number, grade_point_average)
        self.science_work = science_work
