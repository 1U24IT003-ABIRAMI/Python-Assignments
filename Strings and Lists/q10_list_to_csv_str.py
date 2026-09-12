
""" Question 10: list_to_csv_str """
"""
Input: list
Output: string containing each row of list
"""
def list_to_csv_str(L):
    return

""" Test 10 """
def test_list_to_csv_str():
    print("Testing list_to_csv_string...", end='')
    L = [["Alice","Bob","Charlie"],
             [1,2,3],
             [4,5,6]]
    assert(list_to_csv_str(L) == "Alice,Bob,Charlie\n1,2,3\n4,5,6")
    L1 = [["Exam","Grade1","Grade2","Grade3"],
            ["Test",90,85,96],
            ["Quiz",70,70,72],
            ["Final",86,58,92]]
    assert(list_to_csv_str(L1) == "Exam,Grade1,Grade2,Grade3\nTest,90,85,96\nQuiz,70,70,72\nFinal,86,58,92")
    print("... done!")


if __name__ == '__main__':
    test_list_to_csv_str()