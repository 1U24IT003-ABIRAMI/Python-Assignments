""" Question 4: count """
"""
Inputs: two strings, s and t
Output: number of times t occurs in s
"""
def count(s, t):
    return

""" Test 4 """
def test_count():
    print("Testing count...", end='')
    assert(count("Hello", "l") == 2)
    assert(count("pineapple", "p") == 3)
    assert(count("farewell everyone", "are") == 1)
    assert(count("", "aa") == 0)
    assert(count("Hello world", " ") == 1)
    print("... done!")

if __name__ == '__main__':
    test_count()