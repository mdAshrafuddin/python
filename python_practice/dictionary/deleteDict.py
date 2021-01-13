sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}


dicRemove = ['name', 'salary']

sampleDict = {k: sampleDict[k] for k in sampleDict.keys() - dicRemove}

print(sampleDict)