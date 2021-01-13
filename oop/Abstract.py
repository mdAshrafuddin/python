from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    # overriding abstarct method
    def noofsides(self):
        print('I have 5 sides')


# Driver code 
R = Triangle() 
R.noofsides() 