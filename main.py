class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.av_grade_hw = float()
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        number_value = 0
        progress_courses = ", ".join(self.courses_in_progress)
        finish_course = ", ".join(self.finished_courses)
        for i in self.grades:
            number_value += len(self.grades[i])
        self.av_grade_hw = sum(map(sum, self.grades.values()))/number_value
       
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_grade_hw}\nКурсы в процессе изучения: {progress_courses}\nЗавершенные курсы: {finish_course}'
        return result  
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a class Student')
            return
        return self.av_grade_hw < other.av_grade_hw


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.av_grade = float()
        
    def __str__(self):
        number_value = 0
        for i in self.grades:
            number_value += len(self.grades[i])
    
        self.av_grade = sum(map(sum, self.grades.values()))/number_value
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grade}'
        return result  

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a class Lecturer')
            return
        return self.av_grade < other.av_grade


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        input = f"Имя: {self.name}\nФамилия: {self.surname}"
        return input

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('RENO', 'Subway')
lecturer2.courses_attached += ['Git']



super_reviewer = Reviewer("Nikola", "Norvol")
super_reviewer.courses_attached += ['Python']
super_reviewer.courses_attached += ['Git']

super_reviewer2 = Reviewer("Nikola", "Norvol")
super_reviewer2.courses_attached += ['Python']
super_reviewer2.courses_attached += ['Git']


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

best_student2 = Student('May', 'Lion', 'your_gender')
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Введение в программирование']

best_student.rate_lecturer(lecturer1,"Python", 10)
best_student.rate_lecturer(lecturer1,"Python", 8)
best_student.rate_lecturer(lecturer1,"Python", 8)
best_student2.rate_lecturer(lecturer2,"Git", 8)
best_student2.rate_lecturer(lecturer2,"Git", 10)
best_student2.rate_lecturer(lecturer2,"Git", 9)

super_reviewer.rate_hw(best_student, "Python", 10)
super_reviewer.rate_hw(best_student, "Python", 6)
super_reviewer.rate_hw(best_student, "Git", 5)
super_reviewer.rate_hw(best_student, "Git", 8)
super_reviewer2.rate_hw(best_student2, "Python", 10)
super_reviewer2.rate_hw(best_student2, "Python", 9)
super_reviewer2.rate_hw(best_student2, "Git", 8)
super_reviewer2.rate_hw(best_student2, "Git", 7)

list_student = [best_student, best_student2]
list_lecturer = [lecturer1, lecturer2]

def student_rating(list_student, course):
    sum_grades = 0
    len_grades = 0
    
    for student in list_student:
        if course in student.courses_in_progress:
            for number in student.grades[course]:
                sum_grades += number
                len_grades += 1
    result = sum_grades / len_grades
    return result


def lecturer_rating(list_lecturer, course):
    sum_grades = 0
    len_grades = 0
    
    for lecturer in list_lecturer:
        if course in lecturer.courses_attached:
            for number in lecturer.grades[course]:
                sum_grades += number
                len_grades += 1
    result = sum_grades / len_grades
    return result
print("Студенты:")
print(best_student)
print()
print(best_student2)
print()
print(f'Результат сравнения студентов (по средним оценкам за лекции): '
      f'{best_student.name} {best_student.surname} < {best_student2.name} {best_student2.surname} = {best_student > best_student2}')
print()
print("Лекторы:")
print(lecturer1)
print()
print(lecturer2)
print()
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer1.name} {lecturer1.surname} < {lecturer2.name} {lecturer2.surname} = {lecturer1 > lecturer2}')
print()


print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(list_student, 'Python')}")
print()

# Выводим результат подсчета средней оценки по всем лекорам для данного курса
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(list_lecturer, 'Python')}")
print()