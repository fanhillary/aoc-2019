# Name: numValid(start, end)
# Description: Finds amount of number in range(start,end) that have 6 digits, only increasing or equal digits, 
#              and also have multiple adjacent duplicates
# ex) valid numbers: 112222, 133449. invalid numbers: 111111(adjacent duplicate is part of large group of adjacents), 123456, 944234
# Params: start: int - starting bound for range of number to check
#         end: int - end bound for range of numbers to check
# returns: amount of numbers that match the criteria within the range
def numValid(start, end):
    countValid = 0
    currNum = start
    if (start < 100000 and end > 100000):
        currNum = 100000
    
    while (currNum <= end):
        ifDecreasing = False
        adjacentCount = [0] * 10
        currString = str(currNum)
        for i in range(0, 5):
            currDigit = int(currString[i])
            nextDigit = int(currString[i+1])

            # it is a decreasing number, so skip to equal number for remainder of integer
            if (currDigit > nextDigit): 
                currNum = int(populateRest(currString, i))
                ifDecreasing = True
                print('currNum: ' + str(currNum))
                break
            if (currDigit == nextDigit): 
                if not adjacentCount[currDigit]:
                    adjacentCount[currDigit] = 1
                adjacentCount[currDigit] += 1 # counting the number of adjacent numbers in a row
                print(adjacentCount)

        if not ifDecreasing:
            numDuplicates = 0
            for count in adjacentCount:
                if (count > 1):
                    numDuplicates += 1

            if numDuplicates > 1:
                countValid += 1
                print(currNum)

            currNum += 1
    return countValid

            
# Name: populateRest(string, index)
# Description: Given string and index, populate the string starting from given index with the character at the given index
# ex) populateRest(153413, 2) returns 153333
# Params: numString: String - string number to replace characters of
#         index: int - index of the character to replace the remainder of the string with
# Returns: string where [index:] is string[index].

def populateRest(numString, index):
    newString = numString[:index+1]
    for x in range(index+1, 6):
        newString += numString[index]
    return newString



result = numValid(152085,670283)

# result = numValid(152085,156000)
print(result)
# populateRest("152085", 1)
        
