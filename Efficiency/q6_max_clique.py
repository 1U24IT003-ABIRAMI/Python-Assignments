"""Question 6: max_clique """
"""
Input: dictionary G
Output: set of names that form the maximum size clique in G
"""
def all_subsets(S):
    if len(S) == 0:
        return [set()]
    T = S.copy()
    s = T.pop()
    subsets_without_s = all_subsets(T)
    subsets_with_s = list()
    for A in subsets_without_s:
        A_copy = A.copy()
        A_copy.add(s)
        subsets_with_s.append(A_copy)
    return subsets_without_s + subsets_with_s

def max_clique(G):
    s=set(G.keys())
    lst=all_subsets(s)
    L=sorted(lst,key=len,reverse=True)
    for val in L:
        is_clique=True
        for name_1 in val:
            for name_2 in val:
                if G[name_1][name_2]==False:
                    is_clique=False                       
        if is_clique:
            return val

""" Test 6"""  
def test_max_clique():
    print("Testing max_clique...", end="")
    G = {"Alice": {"Alice": True, "Bob": True, "Charlie": True},
          "Bob": {"Alice": True, "Bob": True, "Charlie": False},
          "Charlie": {"Alice": True, "Bob": False, "Charlie": True}}
    assert(max_clique(G) == {"Alice", "Bob"} or max_clique(G) == {"Alice", "Charlie"})

    G1 = {"Tara": {"Tara": True, "Sam": True, "Ryan": True, "Priya": True},
          "Sam": {"Tara": True, "Sam": True, "Ryan": True, "Priya": True},
          "Ryan": {"Tara": True, "Sam": True, "Ryan": True, "Priya": True},
          "Priya": {"Tara": True, "Sam": True, "Ryan": True, "Priya": True}}
    assert(max_clique(G1) == {"Tara", "Sam", "Ryan", "Priya"})
    print("... done!")


if __name__ == '__main__':
    test_max_clique()