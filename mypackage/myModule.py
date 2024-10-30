def top_n(items, n):
    """ Return top n items of an array in desc order

    Args:
        items(array): list or array-like object
        n(int): number of items to return

    Return:
        array: top n items, in desc order

    Eg:
        top_n([8,9,2,1,6], 3)
        [9,8,6]
    """
    sorted_items = sorted(items, reverse=True)
    return sorted_items[:n]