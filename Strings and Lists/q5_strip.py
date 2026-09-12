
""" Question 5: strip """
"""
Input: string s
Output: s with leading and trailing spaces removed
"""
def strip(s):
    return

""" Test 5 """
def test_strip():
    print("Testing strip...", end='')
    assert(strip("Hello") == "Hello") 
    assert(strip(" Hello world ") == "Hello world") 
    assert(strip("      apple ") == "apple") 
    assert(strip("    ") == "") 
    print("... done!")

if __name__ == '__main__':
    test_strip()