def bitStrings(length):
    if not isinstance(length, int): raise TypeError('Expected an intege')
    if length == 0: return []
    if length == 1: return ["0", "1"]
    return [digit + bitstring for digit in bitStrings(1) for bitstring in bitStrings(length -1)]
