a = {'name': 'Ashraf', 'age': 20}

for k, v in a.items():
    print(k, v)

for k, v in enumerate(["Ashraf", "Tanjil"]):
    print(k, v)


questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print("What is your name{0} and {1}". format(q, a))

