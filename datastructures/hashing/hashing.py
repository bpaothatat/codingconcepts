def contains_duplicate(nums: list[int]) -> bool:
    dictionary = {}
    for value in nums:
        if value in dictionary.keys():
            return True
        dictionary[value] = 1
    return False