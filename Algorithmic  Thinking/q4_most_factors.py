""" Question 4: most_factors """
"""
Inputs: two integers, x and y
Output: integer in [x, y] that has the most number of prime factors
        prints out list of all prime factors (not just unique ones)
        ties are resolved in favor of whichever number has the higher sum of factors
"""
def get_factor(n):
    factor=2
    result=list()
    while (factor<=n):
        if n%factor==0:
            result.append(factor)
            n=n//factor
        else:
            factor+=1 
    return result           


def most_factors(x, y):
    big_factor=list()
    big_num=0
    for num in range(x,y+1):
        cur_fact=get_factor(num)
        if len(cur_fact) > len(big_factor):
            big_factor=cur_fact
            big_num=num
        elif len(cur_fact)==len(big_factor):
            if sum(cur_fact)>sum(big_factor):
                big_factor=cur_fact
                big_num=num
    print(big_factor)
    return big_num

""" Test 4 """
def test_most_factors():
    print("Testing most_factors...", end="")
    assert(most_factors(100, 110) == 108) # prints [2, 2, 3, 3, 3]
    assert(most_factors(50, 100) == 96) # prints [2, 2, 2, 2, 2, 3]
    assert(most_factors(20, 24) == 24) # prints [2, 2, 2, 3]
    assert(most_factors(40, 45) == 40) # prints [2, 2, 2, 5]
    assert(most_factors(37, 37) == 37) # prints [37]
    print("... done!")

if __name__ == '__main__':
    test_most_factors()
   
