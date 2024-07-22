class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject

p = Person('John', 20, 'Male')
s = Student('Ian', 42, 'Male', '524534')
t = Teacher('Shailly', 44, 'Female', 'Coding')


print(f'Class: Person. Name: {p.name}. Age: {p.age}. Gender: {p.gender}')
print(f'Class: Student. Name: {s.name}. Age: {s.age}. Gender: {s.gender}. Student ID: {s.student_id}')
print(f'Class: Teacher. Name: {t.name}. Age: {t.age}. Gender: {t.gender}. Subject: {t.subject}')
