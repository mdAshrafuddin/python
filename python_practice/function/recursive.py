def calculateSum(sum):
    if sum:
        return sum + calculateSum(sum-1)
    else:
        return 0
    
recursive = calculateSum(10)
print(recursive)