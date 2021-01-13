class Warehouse:
    purpose = 'storage'
    region  = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()

w2.region = "islam"
print(w2.region)

# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g