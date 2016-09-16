from collections.list import Element, LinkedList
from collections.hashTable import HashTable
from collections.tree import BTree, Node
from utils.sort import BinarySearch, BubbleSort
import os

if __name__ == '__main__':
    hTable = HashTable()

    hTable.put('UDACITY', 'UDACITY')
    hTable.put('UDAVITY', 'Ramayan')

    bTree = BTree()

    arr = [2, 545, 12, 3, 56, 24, 986, 10, 0]

    for ele in arr:
        bTree.add(ele)

    bTree.print_tree(bTree.getRoot())
    node = Node(56)
    print(bTree.search(node).value)
    # print(hTable.get('UDACITY'))
