""" Question 7: nth_fibonacci_number """
"""
Input: integer n
Output: nth fibonacci number
"""
def nth_fibonacci_number(n):
    result1=(1+(5**0.5))/2
    result2=(1-(5**0.5))/2
    final_result=(result1**n- (result2)**n)/(5**0.5)
    print(final_result)
    return round( final_result)
""" Test 7 """
def test_nth_fibonacci_number():
    print("Testing nth_fibonacci_number...", end="")
    assert(nth_fibonacci_number(1) == 1)
    assert(nth_fibonacci_number(3) == 2)
    assert(nth_fibonacci_number(7) == 13)
    assert(nth_fibonacci_number(10) == 55)
    print("... done!")

if __name__ == '__main__':
    test_nth_fibonacci_number()