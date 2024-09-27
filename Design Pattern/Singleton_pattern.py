from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    
    @staticmethod
    @abstractmethod
    def print_data():
        """Implement in child class"""
        

class PersonSingleton(IPerson):
    
    __instance = None
    
    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self, name, age):
        if PersonSingleton.__instance != None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self
            
    @staticmethod
    def print_data():
        print("Name: ", PersonSingleton.__instance.name)
        print("Age: ", PersonSingleton.__instance.age)
        
        
p =PersonSingleton("John", 25)
print(p)
p.print_data()

p2 = PersonSingleton.get_instance()
print(p2)
p2.print_data()