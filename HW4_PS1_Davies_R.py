#Ryan Davies
#1255293
#Homework 4 Program Set 1
#Program to test functions a to j.

# Define constant variables for testing.
TEST_ONE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]		    	
TEST_TWO =  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]   
TEST_THREE = [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]                                                        
TEST_FOUR = [75, 54, 7, 9, 87, 8, 30]                                                        

def main():
    test_cases = [TEST_ONE, TEST_TWO, TEST_THREE, TEST_FOUR] 
    for test_num in range(len(test_cases)):
        print("Run test: ", test_num + 1)
        test_functions(test_cases[test_num])
        print("")

def test_functions(test) :
   print("The original data for all functions is: ", test)

   #a. Demonstrate swapping the first and last element.
   data = list(test)
   swapFirstLast(data)         #call this function      
   print("After swapping first and last: ", data)

   #b. Demonstrate shifting to the right.
   data = list(test)
   shiftRight(data)            #call this function
   print("After shifting right: ", data)

   #c. Demonstrate replacing even elements with zero.
   data = list(test)
   replaceEven(data)           #call this function
   print("After replacing even elements: ", data)

   #d. Demonstrate replacing values with the larger of their neighbors.
   data = list(test)
   replaceNeighbors(data)      #call this function
   print("After replacing with neighbors: ", data)

   #e. Demonstrate removing the middle element.
   data = list(test)
   removeMiddle(data)          #call this function
   print("After removing the middle element(s): ", data)

   #f. Demonstrate moving even elements to the front of the list.
   data = list(test)
   evenToFront(data)           #call this function
   print("After moving even elements: ", data)

   #g. Demonstrate finding the second largest value.
   print("The second largest value is: ", secondLargest(test))

   #h. Demonstrate testing if the list is in increasing order.
   print("The list is in increasing order: ", isIncreasing(test))

   #i. Demonstrate testing if the list contains adjacent duplicates.
   print("The list has adjacent duplicates: ", hasAdjacentDuplicate(test))

   #j. Demonstrate testing if the list contains duplicates.
   print("The list has duplicates: ", hasDuplicate(test))

#Complete the codes for the functions a. to j. below.

#a.
def swapFirstLast(data:list)->None :
    '''Swap the first and last element in a list.'''
    temp = data[0]
    data[0] = data[-1]
    data[-1] = temp

#b.
def shiftRight(data:list) ->None:
    '''Shift the elements to the right.'''
    temp = data.pop(-1)
    data.insert(0, temp)

#c.
def replaceEven(data:list)->None :
    '''Replace all even elements in the list with 0.'''
    for i in range (len(data)):
        if data[i] % 2 == 0:
            data[i] = 0

#d.
def replaceNeighbors(data:list)->None :
    '''Replace each value with the larger of its neighbors.'''
    temp = list(data)
    for i in range (1, len(data)-1):
        if (data[i-1] > data[i+1]):
            data[i] = data[i-1]
        else:
            data[i] = data[i+1]
            

#e.
def removeMiddle(data:list) ->None:
    '''Remove the middle element or elements from a list.'''
    if len(data) % 2 == 0:
        index = int(len(data)/2)-1
        data.pop(index)
        data.pop(index)
    else:
        index = int((len(data)+1)/2)-1
        data.pop(index)

#f.
def evenToFront(data:list) ->None:
    '''Move even elements to the front of the list.'''
    templist = list(data)
    index = 0
    for i in range(len(templist)):
        if templist[i] % 2 == 0:
            temp = data.pop(i)
            data.insert(index, temp)
            index += 1

#g.
def secondLargest(data:list)->int :
    '''Identify the second largest value in a list.
        return the second largest value in the list'''
    largest = 0
    secondLargest = 0
    for value in data:
        if value >= largest:
            secondLargest = largest
            largest = value
        elif value >= secondLargest:
            secondLargest = value
    return secondLargest
   
#h.
def isIncreasing(data:list) -> bool:
    '''Determine whether or not the list is in increasing order.
        return True if the list is in increasing order, False otherwise'''
    temp = 0
    for value in data:
        if value < temp:
            return False
        temp = value
    return True
        
#i.
def hasAdjacentDuplicate(data:list) -> bool:
    '''Determine if the list contains adjacent duplicate elements.
       return True if the list contains adjacent duplicates, False otherwise'''
    initialVal = data[0]
    for i in range (len(data)-1):
        if initialVal == data[i+1]:
            return True
        initialVal = data[i+1]
    return False
            

#j.
def hasDuplicate(data:list)->bool :
    '''Determine if the list contains duplicate elements.
        return True if the list contains duplicates, False otherwise'''
    templist = list(data)
    for i in range (len(data)):
        value = templist.pop(0)
        if value in templist:
            return True
    return False
   
   
if __name__ == "__main__":
    main()


##Run test:  1
##The original data for all functions is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##After swapping first and last:  [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
##After shifting right:  [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##After replacing even elements:  [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
##After replacing with neighbors:  [1, 3, 4, 5, 6, 7, 8, 9, 10, 10]
##After removing the middle element(s):  [1, 2, 3, 4, 7, 8, 9, 10]
##After moving even elements:  [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
##The second largest value is:  9
##The list is in increasing order:  True
##The list has adjacent duplicates:  False
##The list has duplicates:  False
##
##Run test:  2
##The original data for all functions is:  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
##After swapping first and last:  [103, 20, 10, 14, 54, 16, 75, 38, 79, 12]
##After shifting right:  [103, 12, 20, 10, 14, 54, 16, 75, 38, 79]
##After replacing even elements:  [0, 0, 0, 0, 0, 0, 75, 0, 79, 103]
##After replacing with neighbors:  [12, 12, 14, 54, 54, 75, 75, 79, 103, 103]
##After removing the middle element(s):  [12, 20, 10, 14, 75, 38, 79, 103]
##After moving even elements:  [12, 20, 10, 14, 54, 16, 38, 75, 79, 103]
##The second largest value is:  79
##The list is in increasing order:  False
##The list has adjacent duplicates:  False
##The list has duplicates:  False
##
##Run test:  3
##The original data for all functions is:  [1, 25, 25, 4, 5, 4, 7, 60, 9, 10]
##After swapping first and last:  [10, 25, 25, 4, 5, 4, 7, 60, 9, 1]
##After shifting right:  [10, 1, 25, 25, 4, 5, 4, 7, 60, 9]
##After replacing even elements:  [1, 25, 25, 0, 5, 0, 7, 0, 9, 0]
##After replacing with neighbors:  [1, 25, 25, 25, 25, 25, 60, 60, 60, 10]
##After removing the middle element(s):  [1, 25, 25, 4, 7, 60, 9, 10]
##After moving even elements:  [4, 4, 60, 10, 1, 25, 25, 5, 7, 9]
##The second largest value is:  25
##The list is in increasing order:  False
##The list has adjacent duplicates:  True
##The list has duplicates:  True
##
##Run test:  4
##The original data for all functions is:  [75, 54, 7, 9, 87, 8, 30]
##After swapping first and last:  [30, 54, 7, 9, 87, 8, 75]
##After shifting right:  [30, 75, 54, 7, 9, 87, 8]
##After replacing even elements:  [75, 0, 7, 9, 87, 0, 0]
##After replacing with neighbors:  [75, 75, 75, 87, 87, 87, 30]
##After removing the middle element(s):  [75, 54, 7, 87, 8, 30]
##After moving even elements:  [54, 8, 30, 75, 7, 9, 87]
##The second largest value is:  75
##The list is in increasing order:  False
##The list has adjacent duplicates:  False
##The list has duplicates:  False
