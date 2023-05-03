import pytest
from linkedlist import *

def mergeLinkedLists(linkedList_one, linkedList_two):
    """Merge two doubly linked lists that are in sorted order.

    Merge two doubly linked lists that are in sorted order. The merged list will also be in sorted order. The merge is done in place, so the returned linked list is `linkedList_one` with its head updated.

    Args:
        linkedList_one (LinkedList): The first linked list to merge.
        linkedList_two (LinkedList): The second linked list to merge.

    Returns:
        LinkedList: The merged linked list, with its head updated to reflect the new head of the merged list.
    """
    # inicializamos os dois nós que serão iterados em ambas as listas
    n1 = linkedList_one.head
    n2 = linkedList_two.head
    n1Prev = None
    while n2 is not None: # enquanto ainda há nós na segunda lista
      if n1.data < n2.data: # verificamos qual dos nós atuais é o maior. Se for o da segunda lista...
        if n1.next is None: # ...e se estivermos no fim da lista:
          n1.next = n2 # apontamos o último nó da lista 1 (que vai ser o atual) para o primeiro nó do que resta da lista 2
          n2.prev = n1 # e para manter a dupla ligação também apontamos o n1 como sendo o antecessor de n2.
          linkedList_one.length += linkedList_two.length # o resultado será uma lista com o tamanho das duas listas combinadas.
          break # se isto acontecer, podemos parar o loop.
        n1Prev = n1 # se não estivermos no fim da lista, basta irmos para o próximo nó da lista 1 para comparar.
        n1 = n1.next
      else: # se o nó 1 que é maior
        if n1Prev is None: # verificamos primeiro se o n1 é o primeiro nó da lista 1.
          n1Prev = n2 # se for, significa que o primeiro nó da lista 2 deve vir antes dele.
          n2 = n1Prev.next # passamos o iterador da lista 2 para o próximo (considerando que n1Prev ainda é da segunda lista neste momento)
          n1Prev.next = n1 # o próximo nó de n1Prev não será mais um outro nó da segunda lista, mas sim o primeiro nó da lista 1.
          n1.prev = n1Prev # para manter a dupla ligação, o nó anterior ao n1 deve ser registrado como sendo o n1Prev.
          linkedList_one.head = n1Prev # por fim, atualizamos a nova cabeça da lista 1 como sendo o n1Prev.
        else: # se n1 não estiver no início da lista 1:
          n1Prev.next = n2 # o nó n2 deve ficar entre o n1Prev e o n1. Porranto o next do n1Prev deve ser o n2.
          n2 = n2.next # passamos o iterador da lista 2 para o próximo elemento da lista 2 (pode ser nullptr)
          n1Prev.next.next = n1 # como não podemos referenciar o nó que será inserido entre n1Prev e n1 como sendo o n2, configuramos desta maneira a ligação entre ele e n1.
          n1Prev.next.prev = n1Prev # para manter a dupla ligação entre n1Prev e o antigo n2, configuramos assim o prévio ao antigo n2.
          n1.prev = n1Prev.next # também para manter a dupla ligação entre o antigo n2 e o n1, configuramos assim o prévio ao n1.
          n1Prev = n1Prev.next # por fim, atualizamos o prévio ao n1 como sendo o antigo n2.
        linkedList_two.head = n2 # agora esta é a nova cabeça da lista 2.
        linkedList_one.length += 1 # a lista 1 ganhou um elemento
        linkedList_two.length -= 1 # e a lista 2 perdeu um elemento
    return linkedList_one

@pytest.fixture(scope="session")
def data():
    
    array = []
    
    # test 1 data
    array.append([[2,6,7,8],[1,3,4,5,9,10]])

    # test 2 data
    array.append([[1,2,3,4,5],[6,7,8,9,10]])

    # test 3 data
    array.append([[6,7,8,9,10],[1,2,3,4,5]])

    # test 4 data
    array.append([[1,3,5,7,9],[2,4,6,8,10]])

    # test 5 data
    array.append([[0,1,2,3,4,5,7,8,9,10],[6]])

    # test 6 data
    array.append([[6],[0,1,2,3,4,5,7,8,9,10]])

    # test 7 data
    array.append([[1],[2]])

    # test 8 data
    array.append([[2],[1]])

    # test 9 data
    array.append([[1,1,1,3,4,5,5,5,10],[1,1,2,2,5,6,10,10]])
    
    return array

def test_1(data):
    """
    Test evaluation for [[2,6,7,8],[1,3,4,5,9,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[0][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[0][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test


def test_2(data):
    """
    Test evaluation for [[1,2,3,4,5],[6,7,8,9,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[1][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[1][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_3(data):
    """
    Test evaluation for [[6,7,8,9,10],[1,2,3,4,5]]
    """
    linkedlist_one = LinkedList()
    for item in data[2][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[2][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_4(data):
    """
    Test evaluation for [[1,3,5,7,9],[2,4,6,8,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[3][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[3][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_5(data):
    """
    Test evaluation for [[0,1,2,3,4,5,7,8,9,10],[6]]
    """
    linkedlist_one = LinkedList()
    for item in data[4][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[4][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [0,1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_6(data):
    """
    Test evaluation for [[6],[0,1,2,3,4,5,7,8,9,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[5][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[5][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [0,1,2,3,4,5,6,7,8,9,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_7(data):
    """
    Test evaluation for [[1],[2]]
    """
    linkedlist_one = LinkedList()
    for item in data[6][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[6][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_8(data):
    """
    Test evaluation for [[2],[1]]
    """
    linkedlist_one = LinkedList()
    for item in data[7][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[7][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,2]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test

def test_9(data):
    """
    Test evaluation for [[1,1,1,3,4,5,5,5,10],[1,1,2,2,5,6,10,10]]
    """
    linkedlist_one = LinkedList()
    for item in data[8][0]:
      linkedlist_one.append(item)

    linkedlist_two = LinkedList()
    for item in data[8][1]:
      linkedlist_two.append(item)

    linkedlist_test = LinkedList()
    for item in [1,1,1,1,1,2,2,3,4,5,5,5,5,6,10,10,10]:
      linkedlist_test.append(item)

    assert mergeLinkedLists(linkedlist_one, linkedlist_two) == linkedlist_test
