""" Question 2: ends_with """
"""
Inputs: two strings, s and t
Output: True if s ends with t, False otherwise
"""
def ends_with(s, t):
    return

""" Test 2 """
def test_ends_with():
    print("Testing ends_with...", end='')
    assert(ends_with("Hello world", "world") == True)
    assert(ends_with("Hello world", "rld") == True)
    assert(ends_with("rain", "r") == False)
    assert(ends_with("apple", "") == True)
    assert(ends_with("", "abc") == False)
    print("... done!")

if __name__ == '__main__':
    test_ends_with()