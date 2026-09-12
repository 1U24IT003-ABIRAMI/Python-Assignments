""" Question 6: num_lines """
"""
Input: string s
Output: number of lines s contains
"""
def num_lines(s):
    return

""" Test 6 """
def test_num_lines():
    print("Testing num_lines...", end='')
    s = "Hello world"
    assert(num_lines(s) == 1)
    s1 = """ Hello 
                world """
    assert(num_lines(s1) == 2)
    s2 = """    There are
            many lines
            here
            with
            spaces.   """
    assert(num_lines(s2) == 5)
    print("... done!")

if __name__ == '__main__':
    test_num_lines()