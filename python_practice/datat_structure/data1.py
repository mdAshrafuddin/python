listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = list()

oddElements = listOne[1::2]
print(oddElements)
eventElement = listTwo[0::2]
print(eventElement)

listThree.extend(oddElements)
listThree.extend(listTwo)
print(listThree)

