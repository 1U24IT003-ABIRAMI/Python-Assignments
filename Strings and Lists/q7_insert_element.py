
""" Question 7: insert_element """
"""
Inputs: list, index, and element
Output: list with element inserted at index (destructively)
"""
def insert_element(L, i, el):
    return

""" Test 7 """
def test_insert_element():
    print("Testing insert_element...", end='')
    L = [1, 2, 3, 4]
    assert(insert_element(L, 1, 5) == None)
    assert(L == [1, 5, 2, 3, 4])
    L1 = [2, 4, 6]
    assert(insert_element(L1, 5, 0) == None)
    assert(L1 == [2, 4, 6, 0])
    L2 = []
    assert(insert_element(L2, 0, 5) == None)
    assert(L2 == [5])
    print("... done!")

if __name__ == '__main__':
    test_insert_element()