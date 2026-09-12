""" Question 1: starts_with """
"""
Inputs: two strings, s and t, and start index
Output: True if s starts with t starting at specified index, False otherwise
"""
def starts_with(s, t, start):
    return 
    
    
""" Test 1 """
def test_starts_with():
    print("Testing starts_with...", end='')
    assert(starts_with("Hello world", "Hello", 0) == True)
    assert(starts_with("Hello world", "Hello", 3) == False)
    assert(starts_with("butterfly", "fly", 4) == False)
    assert(starts_with("butterfly", "fly", 6) == True)
    assert(starts_with("orange", "", 4) == True)
    assert(starts_with("", "abc", 0) == False)
    print("... done!")

if __name__ == '__main__':
    test_starts_with()