
def QuickSort(array):
    elements = len(array)
    
    #Base case
    if elements < 2:
        return array
    
    current_position = 0 #Position of the partitioning element

    for i in range(1, elements): #Partitioning loop
         if array[i] <= array[0]:
              current_position += 1
              temp = array[i]
              array[i] = array[current_position]
              array[current_position] = temp

    temp = array[0]
    array[0] = array[current_position] 
    array[current_position] = temp #Brings pivot to it's appropriate position
    
    left = QuickSort(array[0:current_position]) #Sorts the elements to the left of pivot
    right = QuickSort(array[current_position+1:elements]) #sorts the elements to the right of pivot

    array = left + [array[current_position]] + right #Merging everything together
    
    return array


def BubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        tmp = array[j]
        array[j] = array[j+1]
        array[j+1] = array[j]
        
  return array

