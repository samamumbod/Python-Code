class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print('Name:', self.name)
        print('Age:', self.age)

class Student(Person):
    def __init__(self, name, age, section):
        super().__init__(name,age)
        self.section = section

    def displayStudent(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Section:', self.section)

person = Person('Mumbod', 22)
person.display()
print('')
student = Student('Mumbod', 22, 'Section 12')
student.displayStudent()
