class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'    
    
    def __average_grade(self):
        mean_grades = []
        for grades_list in self.grades.values():
            mean_grades.append(sum(grades_list) / len(grades_list))
        return sum(mean_grades) / len(mean_grades)

    def __str__(self) -> str:
        return f"""
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.__average_grade()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}
        """
    
    def __lt__(self, other):
        if isinstance(other, Student):
            if self.__average_grade() is not None and other.__average_grade() is not None:
                return self.__average_grade() < other.__average_grade()
            else:
                return 'Ошибка'
        else:
                return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Student):
            if self.__average_grade() is not None and other.__average_grade() is not None:
                return self.__average_grade() > other.__average_grade()
            else:
                return 'Ошибка'
        else:
                return 'Ошибка'

    def __eq__(self, other):
        if isinstance(other, Student):
            if self.__average_grade() is not None and other.__average_grade() is not None:
                return self.__average_grade() == other.__average_grade()
            else:
                return 'Ошибка'
        else:
                return 'Ошибка'

    def __ne__(self, other):
        if  isinstance(other, Student):
            if self.__average_grade() is not None and other.__average_grade() is not None:
                return self.__average_grade() != other.__average_grade()
            else:
                return 'Ошибка'
        else:
                return 'Ошибка'

    def __le__(self, other):
        if isinstance(other, Student):
            if self.__average_grade() is not None and other.__average_grade() is not None:
                return self.__average_grade() <= other.__average_grade()
            else:
                return 'Ошибка'
        else:
                return 'Ошибка'
    
    def __ge__(self, other):
        if isinstance(other, Student):
            if self.__average_grade() is not None and other.__average_grade() is not None:
                return self.__average_grade() >= other.__average_grade()
            else:
                return 'Ошибка'
        else:
                return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_grade(self):
        mean_grades = []
        for grades_list in self.grades.values():
            mean_grades.append(sum(grades_list) / len(grades_list))
        return sum(mean_grades) / len(mean_grades)
       

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}\n"
    
    def __lt__(self, other):
        if isinstance(self, Lecturer) and isinstance(other, Lecturer):
            if self.__average_grade() is not None and other.__average_grade() is not None:
                return self.__average_grade() < other.__average_grade()
            else:
                return 'Ошибка'
        else:
                return 'Ошибка'

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            if self.__average_grade() is not None and other.__average_grade() is not None:
                return self.__average_grade() > other.__average_grade()
            else:
                return 'Ошибка'
        else:
                return 'Ошибка'

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            if self.__average_grade() is not None and other.__average_grade() is not None:
                return self.__average_grade() == other.__average_grade()
            else:
                return 'Ошибка'
        else:
                return 'Ошибка'

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            if self.__average_grade() is not None and other.__average_grade() is not None:
                return self.__average_grade() != other.__average_grade()
            else:
                return 'Ошибка'
        else:
                return 'Ошибка'

    def __le__(self, other):
        if isinstance(other, Lecturer):
            if self.__average_grade() is not None and other.__average_grade() is not None:
                return self.__average_grade() <= other.__average_grade()
            else:
                return 'Ошибка'
        else:
                return 'Ошибка'

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            if self.__average_grade() is not None and other.__average_grade() is not None:
                return self.__average_grade() >= other.__average_grade()
            else:
                return 'Ошибка'
        else:
                return 'Ошибка'

class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"


def average_grade_hw(students, course):
    average_grade = []
    if len(students) > 0:
        for student in students:
            if isinstance(student, Student):
                average_grade += student.grades.get(course)
    return sum(average_grade) / len(average_grade)

def average_grade_lectors(lectors, course):
    average_grade = []
    if len(lectors) > 0:
        for lector in lectors:
            if isinstance(lector, Lecturer):
                average_grade += lector.grades.get(course)
    return sum(average_grade) / len(average_grade)


 
best_student1 = Student('Student', 'One', 'male')
best_student1.courses_in_progress += ['Python', 'JavaScript']
best_student1.finished_courses += ['GoLang']

best_student2 = Student('Student', 'Two', 'female')
best_student2.courses_in_progress += ['Python']
best_student1.finished_courses += ['JavaScript']
 
cool_mentor1 = Mentor('Mentor', 'One')
cool_mentor1.courses_attached += ['Python', 'JavaScript']
 
cool_mentor2 = Mentor('Mentor', 'Two')
cool_mentor2.courses_attached += ['Python']

reviewer1 = Reviewer('Reviewer', 'One')
reviewer1.courses_attached += ['Python', 'JavaScript']

reviewer2 = Reviewer('Reviewer', 'Two')
reviewer2.courses_attached += ['Python']

lector1 = Lecturer('Lecturer', 'One')
lector1.courses_attached += ['Python', 'JavaScript']

lector2 = Lecturer('Lecturer', 'Two')
lector2.courses_attached += ['Python']

reviewer1.rate_hw(best_student1, 'Python', 10)
reviewer1.rate_hw(best_student1, 'Python', 8)
reviewer1.rate_hw(best_student1, 'JavaScript', 7)
reviewer1.rate_hw(best_student1, 'JavaScript', 9)
reviewer2.rate_hw(best_student2, 'Python', 10)
reviewer2.rate_hw(best_student2, 'Python', 5)

best_student1.rate_lector(lector1, 'Python', 10)
best_student1.rate_lector(lector1, 'JavaScript', 10)
best_student2.rate_lector(lector2, 'Python', 10)
best_student1.rate_lector(lector2, 'Python', 10)

print(best_student1 > best_student2)
print(best_student1 < best_student2)
print(best_student1 == best_student2)
print(best_student1 != best_student2)
print(best_student1 <= best_student2)
print(best_student1 >= best_student2)

print(lector1 > lector2)
print(lector1 < lector2)
print(lector1 == lector2)
print(lector1 != lector2)
print(lector1 <= lector2)
print(lector1 >= lector2)

print(best_student1)
print(best_student2)
print(reviewer1)
print(reviewer2)
print(lector1)
print(lector2)

print(average_grade_hw([best_student1, best_student2], 'Python'))
print(average_grade_lectors([lector1, lector2], 'Python'))