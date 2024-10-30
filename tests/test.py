from mypackage import myModule

def test_top_n():
    """"
    make sure top_n works correctly

    """
    assert myModule.top_n([5,2,3,8,7], 3) == [8,7,5], "Incorrect" 
    assert myModule.top_n([13,9,5,7,11], 2) == [13,11,9], "Incorrect" 
    assert myModule.top_n([5,6,3,1,2,9,4,10,7], 5) == [10,9,7,6,5,4], "Incorrect" 