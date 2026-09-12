""" Question 12: longest_bit_run """
"""
Input: string s of 0s and 1s
Output: the length of the longest run of 0s or 1s
"""


def longest_bit_run(s):
    pre_char=""
    cur_count=0
    max_count=0
    for i in s:
        if i==pre_char:
            cur_count+=1
        else:
            cur_count=1
        if cur_count>max_count:
            max_count=cur_count
        pre_char=i            
    return max_count

""" Test 12 """
def test_longest_bit_run():
    print("Testing longest_bit_run...", end='')
    assert(longest_bit_run('0') == 1)
    assert(longest_bit_run('011') == 2)
    assert(longest_bit_run('0000') == 4)
    assert(longest_bit_run('01') == 1)
    assert(longest_bit_run('00111100') == 4)
    print("... done!")


if __name__ == '__main__':
    test_longest_bit_run()