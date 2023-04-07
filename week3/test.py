from stack import *

def sunsetViews(buildings, direction):
    """
    Given an array of buildings and a direction that all of the buildings face,
    return an array of the indices of the buildings that can see the sunset.
    
    A building can see the sunset if it's strictly taller than all of the buildings
    that come after it in the direction that it faces.

    Args:
    buildings (list): A list of positive, non-zero integers representing the heights of the buildings.
    direction (str): A string denoting the direction the buildings face, either 'EAST' or 'WEST'.
    
    Returns:
    list: A sorted list of indices of the buildings that can see the sunset.
    """
    result = Stack()

    if direction == "EAST":
        curMax = buildings[-1]
        start = len(buildings) - 1
        stop = -1
        step = -1
    else:
        curMax = buildings[0]
        start = 0
        stop = len(buildings)
        step = 1
    result.push(start)
    print(curMax, start, stop, step)
    for i in range(start, stop, step):
        if buildings[i] > curMax:
            print(buildings[i], curMax)
            curMax = buildings[i]
            result.push(i)
    return sorted(list(result))

print(sunsetViews([3, 5, 4, 4, 3, 1, 3, 2],"EAST"))