import pytest

def getNthFib(n):
    """
    This function returns the nth number in the Fibonacci sequence, 
    where the first two numbers are 0 and 1, and each subsequent number
    is the sum of the two preceding numbers.

    Parameters:
    n (int): the position of the desired number in the Fibonacci sequence (1-based indexing)

    Returns:
    int: the nth number in the Fibonacci sequence

    Example:
    >>> getNthFib(6)
    5
    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    f0 = 0
    f1 = 1
    nth_number_in_fib_sequence = 0
    for i in range(n - 2):
        nth_number_in_fib_sequence = f1 + f0
        f0 = f1
        f1 = nth_number_in_fib_sequence
    return nth_number_in_fib_sequence


@pytest.fixture(scope="session")
def data():
    
    array = [6,1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18]
    return array

def test_1(data):
    """
    Test evaluation for n = 6
    """
    assert getNthFib(data[0]) == 5

def test_2(data):
    """
    Test evaluation for n = 1
    """
    assert getNthFib(data[1]) == 0

def test_3(data):
    """
    Test evaluation for n = 2
    """
    assert getNthFib(data[2]) == 1

def test_4(data):
    """
    Test evaluation for n = 3
    """
    assert getNthFib(data[3]) == 1

def test_5(data):
    """
    Test evaluation for n = 4
    """
    assert getNthFib(data[4]) == 2

def test_6(data):
    """
    Test evaluation for n = 5
    """
    assert getNthFib(data[5]) == 3

def test_7(data):
    """
    Test evaluation for n = 7
    """
    assert getNthFib(data[6]) == 8

def test_8(data):
    """
    Test evaluation for n = 8
    """
    assert getNthFib(data[7]) == 13

def test_9(data):
    """
    Test evaluation for n = 9
    """
    assert getNthFib(data[8]) == 21

def test_10(data):
    """
    Test evaluation for n = 10
    """
    assert getNthFib(data[9]) == 34

def test_11(data):
    """
    Test evaluation for n = 11
    """
    assert getNthFib(data[10]) == 55

def test_12(data):
    """
    Test evaluation for n = 12
    """
    assert getNthFib(data[11]) == 89

def test_13(data):
    """
    Test evaluation for n = 13
    """
    assert getNthFib(data[12]) == 144

def test_14(data):
    """
    Test evaluation for n = 14
    """
    assert getNthFib(data[13]) == 233

def test_15(data):
    """
    Test evaluation for n = 15
    """
    assert getNthFib(data[14]) == 377

def test_16(data):
    """
    Test evaluation for n = 16
    """
    assert getNthFib(data[15]) == 610

def test_17(data):
    """
    Test evaluation for n = 17
    """
    assert getNthFib(data[16]) == 987

def test_18(data):
    """
    Test evaluation for n = 18
    """
    assert getNthFib(data[17]) == 1597
