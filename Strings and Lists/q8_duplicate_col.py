
""" Question 8: duplicate_col """
"""
Inputs: list, index, and integer n
Output: list with column at specified index duplicated n times
"""
def duplicate_col(L, index, n):
    return

""" Test 8 """
def test_duplicate_col():
    print("Testing duplicate_col...", end='')
    L = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    res = [[1, 1, 1, 2, 3],
            [4, 4, 4, 5, 6],
            [7, 7, 7, 8, 9]]
    assert(duplicate_col(L, 0, 2) == None)
    assert(L == res)
    L1 = [[2, 4],
          [6, 8]]
    res1 = [[2, 4, 4, 4, 4],
            [6, 8, 8, 8, 8]]
    assert(duplicate_col(L1, 1, 3) == None)
    assert(L1 == res1)
    L2 = [[1, 3],
            [2, 4],
            [3, 5]]
    res2 = [[1, 3],
            [2, 4],
            [3, 5]]
    assert(duplicate_col(L2, 0, 0) == None)
    assert(L2 == res2)
    print("... done!")


if __name__ == '__main__':
    test_duplicate_col()