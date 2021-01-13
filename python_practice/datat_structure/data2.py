sampleList = [34, 54, 67, 89, 11, 43, 94]

print('Orginal list: ', sampleList)
element =  sampleList.pop(4)
sampleList.insert(2, 120)
print('List After adding element at index: ', sampleList)
sampleList.append(element)
print('List After Removing element at index: ', sampleList)