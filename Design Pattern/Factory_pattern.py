from abc import ABCMeta, abstractmethod

class Iperson(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def person_method():
        """Interface method"""

class Student(Iperson):
    
    def __init__(self):
        self.name = "Basic Student Name"
        
    def person_method(self):
        print("I am a student")


class Teacher(Iperson):
        
    def __init__(self):
        self.name = "Basic Teacher Name" 
        
    def person_method(self):
        print("I am a teacher")
        

class PersonFactory:
    
    @staticmethod
    def build_person(person_type):
        if person_type == "student":
            return Student()
        elif person_type == "teacher":
            return Teacher()
        else:
            raise ValueError("Invalid Person Type")       
    
    
if __name__ == "__main__":
    choice = input("Enter the person type: ")
    person = PersonFactory.build_person(choice)
    person.person_method()

