import pytest
from binarysearchtree import *

def validateThreeNodes(bst:BST, valueOne, valueTwo, valueThree):
    """
    Checks if the given three nodes have the required relationship in the Binary Search Tree.

    This function validates if either nodeTwo is a descendant of nodeOne and nodeThree is a descendant
    of nodeTwo, or if nodeOne is a descendant of nodeTwo and nodeThree is an ascendant of nodeTwo.

    Parameters:
    bst (BST): The Binary Search Tree containing the nodes.
    valueOne (int): The value of the first node.
    valueTwo (int): The value of the second node.
    valueThree (int): The value of the third node.

    Returns:
    bool: True if the given nodes have the required relationship, False otherwise.
    """
    def lookFor(node:Node, f1:bool, f2:bool, f3:bool) -> bool:
        if node == None:
            return False
        elif node.value == valueOne:
            if not f3:
                if valueThree > valueOne:
                    return lookFor(node.right_child, True, False, False)
                else:
                    return lookFor(node.left_child, True, False, False)
            else:
                if f2:
                    return True
                else:
                    return False
        elif node.value == valueThree:
            if not f1:
                if valueOne > valueThree:
                    return lookFor(node.right_child, False, False, True)
                else:
                    return lookFor(node.left_child, False, False, True)
            else:
                if f2:
                    return True
                else:
                    return False
        elif node.value == valueTwo:
            if not f1 and not f3:
                return False
            elif not f1 and f3:
                if valueOne > valueTwo:
                    return lookFor(node.right_child, False, True, True)
                else:
                    return lookFor(node.left_child, False, True, True)
            else:
                if valueThree > valueTwo:
                    return lookFor(node.right_child, True, True, False)
                else:
                    return lookFor(node.left_child, True, True, False)
        else:
            if f1:
                if valueThree > node.value:
                    return lookFor(node.right_child, True, f2, False)
                else:
                    return lookFor(node.left_child, True, f2, False)
            elif f3:
                if valueOne > node.value:
                    return lookFor(node.right_child, False, f2, True)
                else:
                    return lookFor(node.left_child, False, f2, True)
            else:
                if valueOne > node.value and valueThree > node.value:
                    return lookFor(node.right_child, False, False, False)
                elif valueOne < node.value and valueThree < node.value:
                    return lookFor(node.left_child, False, False, False)
                else:
                    return False
    return lookFor(bst.root, False, False, False)


@pytest.fixture(scope="session")
def data():
    
    array = [[5, 2, 1, 0, 4, 3, 7, 6, 8],
             [5, 3, 2, 1, 0, 4, 7, 6, 8],
             [5, 3, 2, 1, 0, 4, 7, 6, 8],
             [2, 1, 3, 4, 5, 6, 7, 8, 9],
             [6, 4, 3, 1, 2, 8, 7, 9],
             [2, 1, 3, 4],
             [8, 4, 3, 2, 1, 10, 9, 14, 12, 11, 6, 7, 13],
             [8, 7, 6, 5, 4, 3, 2, 1, 9],
             [3, 2, 1],
             [3, 2, 1],
             [6, 4, 2, 1, 3, 5, 8, 7, 9],
             [10, 6, 5, 3, 1, 2, 4, 8, 7, 9, 15, 14, 13, 11, 12, 18, 17, 16],
             [10, 6, 5, 3, 1, 2, 4, 8, 7, 9, 15, 14, 13, 11, 12, 18, 17, 16],
             [5, 3, 1, 0, 2, 4, 7, 6, 8],
             [5, 3, 1, 0, 2, 4, 7, 6, 8]]
    return array

def test_1(data):
    """
    Test evaluation for "nodeOne": "5","nodeThree": "3","nodeTwo": "2"
    """
    bst = BST()
    for value in data[0]:
      bst.add(value)
    assert validateThreeNodes(bst,5,2,3) == True

def test_2(data):
    """
    Test evaluation for "nodeOne": "5", "nodeThree": "1", "nodeTwo": "8",
    """
    bst = BST()
    for value in data[1]:
        bst.add(value)
    assert validateThreeNodes(bst,5,8,1) == False

def test_3(data):
    """
    Test evaluation for   "nodeOne": "8","nodeThree": "2","nodeTwo": "5",
    """
    bst = BST()
    for value in data[2]:
        bst.add(value)
    assert validateThreeNodes(bst,8,5,2) == False

def test_4(data):
    """
    Test evaluation for  "nodeOne": "2","nodeThree": "8","nodeTwo": "5"
    """
    bst = BST()
    for value in data[3]:
        bst.add(value)
    assert validateThreeNodes(bst,2,5,8) == True

def test_5(data):
    """
    Test evaluation for "nodeOne": "4", "nodeThree": "2", "nodeTwo": "1",
    """
    bst = BST()
    for value in data[4]:
        bst.add(value)
    assert validateThreeNodes(bst,4,1,2) == True

def test_6(data):
    """
    Test evaluation for "nodeOne": "1","nodeThree": "3","nodeTwo": "2",
    """
    bst = BST()
    for value in data[5]:
        bst.add(value)
    assert validateThreeNodes(bst,1,2,3) == False

def test_7(data):
    """
    Test evaluation for "nodeOne": "2","nodeThree": "13","nodeTwo": "4"
    """
    bst = BST()
    for value in data[6]:
        bst.add(value)
    assert validateThreeNodes(bst,2,4,13) == False

def test_8(data):
    """
    Test evaluation for "nodeOne": "8","nodeThree": "1","nodeTwo": "7"
    """
    bst = BST()
    for value in data[7]:
        bst.add(value)
    assert validateThreeNodes(bst,8,7,1) == True

def test_9(data):
    """
    Test evaluation for "nodeOne": "2","nodeThree": "3","nodeTwo": "1"
    """
    bst = BST()
    for value in data[8]:
        bst.add(value)
    assert validateThreeNodes(bst,2,1,3) == False

def test_10(data):
    """
    Test evaluation for "nodeOne": "1", "nodeThree": "3", "nodeTwo": "2"
    """
    bst = BST()
    for value in data[9]:
        bst.add(value)
    assert validateThreeNodes(bst,1,2,3) == True

def test_11(data):
    """
    Test evaluation for "nodeOne": "9","nodeThree": "6","nodeTwo": "8"
    """
    bst = BST()
    for value in data[10]:
        bst.add(value)
    assert validateThreeNodes(bst,9,8,6) == True

def test_12(data):
    """
    Test evaluation for "nodeOne": "12","nodeThree": "15","nodeTwo": "13"
    """
    bst = BST()
    for value in data[11]:
        bst.add(value)
    assert validateThreeNodes(bst,12,13,15) == True

def test_13(data):
    """
    Test evaluation for "nodeOne": "5","nodeThree": "15","nodeTwo": "10"
    """
    bst = BST()
    for value in data[12]:
        bst.add(value)
    assert validateThreeNodes(bst,5,10,15) == False

def test_14(data):
    """
    Test evaluation for "nodeOne": "5","nodeThree": "4","nodeTwo": "3"
    """
    bst = BST()
    for value in data[13]:
        bst.add(value)
    assert validateThreeNodes(bst,5,3,4) == True

def test_15(data):
    """
    Test evaluation for "nodeOne": "5","nodeThree": "1","nodeTwo": "3"
    """
    bst = BST()
    for value in data[14]:
        bst.add(value)
    assert validateThreeNodes(bst,5,3,1) == True
