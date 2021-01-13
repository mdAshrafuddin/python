# Python program to demonstrate 
# overriding in multiple inheritance 

# Defining class name
class Parent1:
    # Constructor
    def __init__(self, name, id):
        self.name = name 
        self.id   = id
    # Create parent's method
    def show(self):
        return self.name

class Child(Parent1):
    def __init__(self, name, id, email):
        super().__init__(name, id)
        self.email = email

    def show(self):
        return '{0} {1} {2}'.format(self.name, self.email, self.id)

ob_parent = Parent1('ashraf', 2345)
ob_chlid  = Child('tanjil', 2345, 'Ashraf@gmail.com')
print(ob_parent.show())
print(ob_chlid.show())