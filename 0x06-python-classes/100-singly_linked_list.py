#!/usr/bin/python3

""" Define a Linked list"""


class Node():
    """Represent A Linked List Node"""
    def __init__(self, data, next_node=None):
        """Initailaize a new Node

        Args:
            data (int): Node Data
            next_node (object): the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList():
    """Represent A Linked List"""
    def __init__(self):
        """Initailaize a new List"""
        self.__head = None

    def __str__(self):
        tmp = self.__head

        while tmp.next_node:
            print("{}".format(tmp.data))
            tmp = tmp.next_node
        return "{}".format(tmp.data)

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node

        elif self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            tmp = self.__head

            while tmp.next_node and tmp.next_node.data < value:
                tmp = tmp.next_node

            new_node.next_node = tmp.next_node
            tmp.next_node = new_node
