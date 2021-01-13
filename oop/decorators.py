def make_pretty(func):
    def inner():
        print('I got decorators')
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()

# pretty = make_pretty(ordnary)

# pretty()