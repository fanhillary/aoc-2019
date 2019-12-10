# Name: numValid(start, end)
# Description: Finds amount of number in range(start,end) that have 6 digits, only increasing or equal digits, and also have adjacent duplicates
# ex) valid numbers: 111111, 133459. invalid numbers: 123456, 944234
# Params: start: int - starting bound for range of number to check
#         end: int - end bound for range of numbers to check
# returns: amount of numbers that match the criteria within the range
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

# result = numValid(152085,157000)
print(result)
# populateRest("152085", 1)
        
