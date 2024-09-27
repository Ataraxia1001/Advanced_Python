from abc import ABCMeta, abstractmethod


class Iperson(metaclass=ABCMeta):
        
    @staticmethod
    @abstractmethod
    def person_method():
        """Interface method"""
        
        
class Person(Iperson):
    
    def person_method(self):
        print("I am a person!")
        

class ProxyPerson(Iperson):
    
    def __init__(self):
        self.person = Person()
        
    def person_method(self):
        print("I am a proxy functionality!")
        self.person.person_method()
        

p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()
        