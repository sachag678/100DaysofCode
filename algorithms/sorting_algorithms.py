"""Sorting"""
import numpy as np
import unittest
import time
from search_algorithms import timer

@timer
def selection_sort(deck):
    """Sorts using selection sort."""
    for firstIndex in range(len(deck)):
        min_index = simple_index_of_min(deck, firstIndex)
        deck = swap(deck, firstIndex, min_index)
    return deck

def index_of_min(deck, firstIndex):
    """Return the index of the smallest element in the subarray.
        This is slower than simple_index_of_min because it is O(n) + O(how long deck.index takes) as opposed to
        O(n).
    """
    return deck.index(np.min(deck[firstIndex:]))

def simple_index_of_min(deck, firstIndex):
    """Return the index of the smallest element in the subarray."""
    min_val = deck[firstIndex] 
    min_idx = firstIndex
    for i in range(firstIndex + 1, len(deck)):
        if min_val > deck[i]:
            min_val = deck[i]
            min_idx = i
    return min_idx

def swap(deck, firstIndex, secondIndex):
    """Swaps the positions of the elements."""
    deck[firstIndex], deck[secondIndex] = deck[secondIndex], deck[firstIndex]
    return deck

@timer
def insertion_sort(deck):
    """Sort deck using insertion sort."""
    for i in range(len(deck)):
        deck = insert(deck, i, deck[i])
    return deck

def insert(deck, rightIndex, value):
    """Inserts the value at the rightIndex."""
    for i in reversed(range(rightIndex)):
        if deck[i] > value:
            swap(deck,i,rightIndex)
            rightIndex-=1
    return deck

def merge_sort(deck, start, end):
    if end>start:
        mid = (start + end) // 2
        merge_sort(deck, start, mid)
        merge_sort(deck, mid + 1, end)
        merge(deck, start, mid, end)
    
    return deck

def merge(deck, start, mid, end):
    """Merges the separate portions of sorted decks."""
    lowhalf = deck[start:mid+1]
    highhalf = deck[mid+1:end+1]

    i = 0
    j = 0
    for index in range(start, end+1):
        if j<len(highhalf) and i<len(lowhalf):
            if lowhalf[i]<highhalf[j]:
                deck[index] = lowhalf[i]
                i+=1
            else:
                deck[index] = highhalf[j]
                j+=1
        else:
            if j>=len(highhalf):
                deck[index] = lowhalf[i]
                i += 1
            elif i>=len(lowhalf):
                deck[index] = highhalf[j]
                j += 1

class TestSorting(unittest.TestCase):
    def setUp(self):
        self.deck = [22, 11, 99, 88, 9, 7, 42, 4]
 
    def test_selection_sort(self):
        self.assertEqual(selection_sort(self.deck), [4, 7, 9, 11, 22, 42, 88, 99])

    def test_insert_sort(self):
        self.assertEqual(insertion_sort(self.deck), [4, 7, 9, 11, 22, 42, 88, 99])
    
    def test_merge(self):
        self.assertEqual(merge_sort(self.deck, 0, len(self.deck)-1), [4, 7, 9, 11, 22, 42, 88, 99])

    
if __name__ == '__main__':
    # unittest.main()
    deck = np.random.randint(0, 1000, (5000, 1))

    selection_sort(deck)
    insertion_sort(deck)
    begin = time.time()
    merge_sort(deck, 0, len(deck) - 1)
    print('merge_sort',': ', (time.time()-begin)*1000.0)