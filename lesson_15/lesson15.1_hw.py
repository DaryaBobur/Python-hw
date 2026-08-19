class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Gender: {self.gender}, age:{self.age}, {self.first_name} {self.last_name}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"Gender: {self.gender}, age: {self.age}, {self.first_name} {self.last_name}, record book: {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.__group = set()

    def add_student(self, student):
        if len(self.__group) >= 10:
            raise ValueError("There can be only 10 students in the group.")
        else:
            self.__group.add(student)

    def delete_student(self, last_name):
        remove_student = self.find_student(last_name)
        if remove_student:
            self.__group.remove(remove_student)

    def find_student(self, last_name):
        for student in self.__group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.__group:
            all_students += str(student) + "\n"
        return f'Number:{self.number}\n {all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 21, 'Emma', 'Brown', 'CD317')
st4 = Student('Male', 24, 'Daniel', 'Wilson', 'EF428')
st5 = Student('Female', 23, 'Sophie', 'Miller', 'GH512')
st6 = Student('Male', 26, 'Michael', 'Davis', 'JK639')
st7 = Student('Female', 20, 'Olivia', 'Anderson', 'LM745')
st8 = Student('Male', 27, 'James', 'Thomas', 'NP856')
st9 = Student('Female', 22, 'Anna', 'Moore', 'QR963')
st10 = Student('Male', 23, 'Alex', 'Martin', 'ST174')
st11 = Student('Female', 25, 'Liza', 'Black', 'AN145')
st12 = Student('Male', 22, 'John', 'Smith', 'BK231')
gr = Group('PD1')
print(gr)

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
    gr.add_student(st12)

except ValueError as e:
    print(e)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку повинен повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!