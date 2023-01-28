#!/usr/bin/python3
"""This module contains the class Node that defines a node of a
singly linked list and also a class SinglyLinkedList that defines
singly linked list.
"""


class Node:
    """This is a class that defines a node of a singly linked list.
    """
    def __init__(self, data, next_node=None):
        """Constructor of the Node instances.

        Args:
            data (int): an integer to stored in the Node object.
            next_node (Node or None): another Node object to be stored in
                the new one.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter and setter for the data property.
        """
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """getter and setter for the next_node attribute..
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Simple singly linked list class.
    """
    def __init__(self):
        """constructor of the SinglyLinkedList class.
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in
        the list(increasing order).

        Args:
            value (Node): Node object to insert.

        Returns:
            None
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        ptr = self.__head
        if value < ptr.data:
            new.next_node = ptr
            self.__head = new
            return
        while ptr.next_node is not None:
            if value <= ptr.next_node.data:
                new.next_node = ptr.next_node
                ptr.next_node = new
                return
            ptr = ptr.next_node
        ptr.next_node = new
        return

    def __str__(self):
        """Returns a string representation of the sll.
        """
        ptr = self.__head
        ret = ""
        while ptr is not None:
            ret += f"{ptr.data}" if ptr.next_node is None else f"{ptr.data}" \
                   + "\n"
            ptr = ptr.next_node

        return ret
