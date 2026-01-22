from dataclasses import dataclass

# traditional classes do not require decorators
# create a student dataclass with @dataclass as a decorator
@dataclass
class Student:
    # dataclasses don't require an __init__ function like traditional classes do
    # save the object's instance variables within main part of dataclass
    # don't need self. to initialize these, but you do need to define their data types
    name: str
    school_id: str
    gpa: float

    # dataclasses will return str on their own
    # but __str__ can make strings returned cleaner
    def __str__(self):
        # return string with object's variables
        return f'Name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'

# main function to create student objects in
def main():
    # create new student object with name, id, and gpa
    alex = Student('Alex', 'abcef', 3.5)
    # print out each object variable
    print(alex.name)
    print(alex.school_id)
    print(alex.gpa)
    # call print and the object to print returned string including name, id, and gpa
    print(alex)

    # create new student object with name, id, and gpa
    sam = Student('Sam', 'qwerty', 2.8)
    # print sam object with name, id, and gpa
    print(sam)

# execute main function
if __name__ == '__main__':
    main()