# Bubble sort in Python

import random
import sortlib


def test_BubbleSort():
    data = [random.randint(0,100) for i in range(10)]
    data = sortlib.BubbleSort(data)
    print('[BubbleSort] Sorted Array in Ascending Order:')
    print(data)
    
    assert False

def test_QuickSort():
    data = [random.randint(0,100) for i in range(10)]
    data = sortlib.QuickSort(data)
    print('[QickSort] Sorted Array in Ascending Order:')
    print(data)

test_BubbleSort()
test_QuickSort()

