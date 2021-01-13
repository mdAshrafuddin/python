def decorators_fun(func):
	def inner_fun():
		print('inner function')
		func()
	return inner_fun

@decorators_fun
def simple_fun():
	print('simple function')

simple_fun()

# decor = decorators_fun(simple_fun)

# decor()

def decorator(function):
	def wrapper():
		print('hi')
		function()
		print('Nice Good')
	return wrapper

@decorator
def def_fun():
	print('Good boy')

def_fun()
# de = decorator(def_fun)
# de()

def outerFun():
	print('Outer Function')
	def innerFun():
		print('inner Fun')
	innerFun()
outerFun()




def Decorators_name(func):
	def InnerDef(name):
		return name.upper()
	return InnerDef

@Decorators_name
def get_text(name):
	return name
# text_dec = Decorators_name(get_text)
print(get_text('ashraf'))




def MyDec(func):
	def Inner_fun(name, age, roll):
		return name, age, roll
	return Inner_fun

@MyDec
def My_fun(name, age):
	return name, age

# d = MyDec(My_fun)
print(My_fun('as', 23, 32929))





