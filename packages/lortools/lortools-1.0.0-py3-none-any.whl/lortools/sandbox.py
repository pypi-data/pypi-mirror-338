"""

.. codeauthor:: Laurent Mertens <laurent.mertens@kuleuven.be>
"""
import sys
sys.setrecursionlimit(100000)

from lortools.array.c_array import IntCArray
from lortools.search.c_binary_search import IntBinarySearch
from lortools.sort.c_quicksort import CQuickSort, CQuickSortMulti

if __name__ == '__main__':
    l = [100-i for i in range(100)]
    b = [200-i for i in range(100)]
    a = IntCArray(size=len(l), data=l)
    b = IntCArray(size=len(b), data=b)
    print(a.get_data())
    print(b.get_data())

    CQuickSort.sort(a)
    print(a.get_data())
    print(b.get_data())

    print(IntBinarySearch.find(a, 50))

    # Check larger ranges
    # import random
    # a = [random.randint(0, 100000) for _ in range(10000)]
    # a = IntCArray(size=10000, data=a)
    # CQuickSort.sort(a)
