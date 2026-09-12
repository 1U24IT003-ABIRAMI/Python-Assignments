""" Question 3: find """
"""
Inputs: two strings, s and t, and start index
Output: first index in s that t appears, searching from start
        -1 if t does not appear in s
"""
def find(s, t, start):
    
    return

""" Test 3 """
def test_find():
    print("Testing find...", end='')
    assert(find("Hello", "ello", 0) == 1)
    assert(find("Hello world", "wor", 2) == 6)
    assert(find("goodbye", "bye", 5) == -1)
    assert(find("goodbye", "bye", 1) == 4)
    assert(find("rainbow", "rainbow", 0) == 0)
    assert(find("", "x", 0) == -1)
    print("... done!")

if __name__ == '__main__':
    test_find()