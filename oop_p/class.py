class MyClass:
    def __init__(self, name, company):
        self.name = name
        self.company = company
    
    def get_all(self):
        return self.name, self.company

    def set_all(self, name, company):
        self.name = name
        self.company = company
    
n = MyClass("Ashraf", "Ashraf.limit")
print(f"My name is {n.name} and company name {n.company}")
print("=" * 25)
n.set_all("Tanjil Chowdhury", 'Chowdhry Company')
print(f"{n.get_all()}")

n.counter = 1
while n.counter < 40:
    n.counter = n.counter * 2
print(n.counter)
del n.counter
