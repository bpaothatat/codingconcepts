def isArraySorted(array):
    if not isinstance(array, list):
        raise TypeError('Expected a list')
    if len(array) <= 1:
        return True
    return array[0] <= array[1] and isArraySorted(array[1:])