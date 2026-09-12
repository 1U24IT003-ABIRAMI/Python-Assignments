""" Question 5: complete_friendship """
"""
Input: dictionary of dictionaries representing friendships
Output: dictionary of all symmetric friendship relationships
"""
import copy

def complete_friendship(d):
    copy_d=copy.deepcopy(d)
    for name in copy_d:
        for friend in copy_d[name]:
            if friend in d:
                d[friend].add(name)
            else:
                d[friend]=set([name])

""" Test 5 """
def test_complete_friendship():
    print("Testing complete_friendship...", end='')
    d = {"alice": {"bob", "charlie"},
         "eve": {"alice"}}
    res = {"alice": {"eve", "bob", "charlie"}, 
            "eve": {"alice"}, 
            "bob": {"alice"}, 
            "charlie": {"alice"}}
    assert(complete_friendship(d) == None)
    assert(d == res)

    d1 = {"frank": {"giselle", "karen"},
            "giselle": {"frank", "karen"},
            "karen": set()}
    res1 = {"frank": {"giselle", "karen"},
            "giselle": {"frank", "karen"},
            "karen": {"frank", "giselle"}}
    assert(complete_friendship(d1) == None)
    assert(d1 == res1)
    print("... done!")

if __name__ == '__main__':
    test_complete_friendship()