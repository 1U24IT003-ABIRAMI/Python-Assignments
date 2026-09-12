""" Question 9: get_averages_from_csv """
"""
Input: two strings, one representing a csv and one representing a header
Output: average of csv entries under header
        None if header does not appear in csv or if values in column are not integers
"""
def get_averages_from_csv(csv_str, header):
    return

""" Test 9 """
def test_get_averages_from_csv():
    print("Testing get_averages_from_csv...", end='')
    csv = """University,Number of Students,Tuition
Carnegie Mellon University,13961,76760
Stanford University,16914,78218
Harvard University,22947,75891
University of California Berkeley,45057,41528"""
    assert(get_averages_from_csv(csv, "Number of Students") == 24719.75)
    assert(get_averages_from_csv(csv, "University") == None)
    assert(get_averages_from_csv(csv, "Tuition") == 68099.25)
    assert(get_averages_from_csv(csv, "Undergrad Population") == None)
    print("... done!")

if __name__ == '__main__':
    test_get_averages_from_csv()