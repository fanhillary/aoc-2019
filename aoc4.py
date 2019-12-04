def numValid(start, end):
    countValid = 0
    currNum = start
    if (start < 100000 and end > 100000):
        currNum = 100000
    
    while (currNum < end):
        ifDuplicate = False
        ifDecreasing = False
        currString = str(currNum)
        for i in range(0, 5):
            currInt = int(currString[i])
            nextInt = int(currString[i+1])

            # it is a decreasing number, so skip to equal number for remainder of integer
            if (currInt > nextInt): 
                currNum = int(populateRest(currString, i))
                ifDecreasing = True
                break
            if (currInt == nextInt): 
                ifDuplicate = True

        if not ifDecreasing:
            if ifDuplicate:
                countValid = countValid + 1
                print(currNum)

            currNum = currNum + 1
    return countValid

            

def populateRest(string, index):
    newString = string[:index+1]
    for x in range(index+1, 6):
        newString += string[index]
    return newString

result = numValid(152085,670283)

# result = numValid(152085,157000)
print(result)
# populateRest("152085", 1)
        
