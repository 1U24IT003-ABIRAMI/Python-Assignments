  
""" Question 7: index_range """
"""
Inputs: list L and integer target
Output: indexes where target first and last appears in L
"""
def binary_range(L, target):      
    start = 0
    end = len(L) - 1           
    while(start <= end):
        middle = (start + end)//2
        if(L[middle] == target): 
            return True
        elif(L[middle] > target): 
            end = middle-1
        else: 
            start = middle+1
    return False
def find_lower(L,target):
    start = 0
    end = len(L) - 1           
    while(start <= end):
        middle = (start + end)//2
        if(L[middle] >= target): 
            end = middle-1
        else: 
            start = middle+1
    return start
def find_upper(L,target):
    start = 0
    end = len(L) - 1           
    while(start <= end):
        middle = (start + end)//2
        if(L[middle] > target): 
            end = middle-1
        else: 
            start = middle+1
    return start-1
def index_range(L, target):
  if not binary_range(L,target):
    return [-1,-1]
  lower=find_lower(L,target)
  upper=find_upper(L,target)
  return [lower,upper]
  


""" Test 7"""  
def test_index_range():
    print("Testing index_range...", end="")
    assert(index_range([1, 1, 2, 3, 3, 3], 1) == [0, 1])
    assert(index_range([1, 1, 2, 3, 3, 3], 2) == [2, 2])
    assert(index_range([1, 1, 2, 3, 3, 3], 3) == [3, 5])
    assert(index_range([1, 1, 2, 3, 3, 3], 4) == [-1, -1])
    print("Passed!")


if __name__ == '__main__':
    test_index_range()