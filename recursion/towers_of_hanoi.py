from sys import setprofile


def TowerOfHanoi(numberOfDisk:int):
    return TowerOfHanoiHelper(numberOfDisk, steps=[])

def TowerOfHanoiHelper(numberOfDisk:int, startPeg:int = 1, endPeg:int=3, steps=[]):
    if not isinstance(numberOfDisk, int) or numberOfDisk < 0:
        raise TypeError("Expected integer greater than -1")
    if numberOfDisk:
        TowerOfHanoiHelper(numberOfDisk-1, startPeg, 6-startPeg-endPeg, steps)
        steps.append((numberOfDisk, startPeg, endPeg))
        TowerOfHanoiHelper(numberOfDisk-1, 6-startPeg-endPeg, endPeg, steps)
    return steps