#!/usr/bin/python3
"""Defines the classes Node and SinglyLinkedList"""


class Node:
    """
    Defines properties Node.

    Attributes:
        data: data field of node.
    """

    def __init__(self, data, next_node=None):
        """New instances of node.

        Args:
            __data : data field of node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data field instance.

        Returns: the data field of a node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Property setter for data.

        Args:
            value (int): data field of a node.

        Raises:
            TypeError: data must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next_node instance.

        Returns: The next_node instance.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Property setter for Node.

        Args:
            value (None): next node of a Node.

        Raises:
            TypeError: next_node must be a Node object .
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """Represents the class object as a string.

        Returns: The class object represented as a string.
        """
        return str(self.data)


class SinglyLinkedList:
    """
    Defines properties of SinglyLinkedList.

    Attributes:
        head: head of the SinglyLinkedList.
    """

    def __init__(self):
        """New instances of SinglyLinkedList .

        Args:
            __head : head of the SinglyLinkedList .
        """
        self.__head = None

    def __str__(self):
        """Represents the class objects as a string.

        Returns: The class object represented as a string.
        """
        print_node = self.get_sorted_nodes()
        return "\n".join(map(str, print_node))

    def get_sorted_nodes(self):
        """Returns the nodes in the linked list in sorted order.

        Returns:
            sorted_nodes: List of nodes in sorted order.
        """
        nodes = []
        tmp_var = self.__head
        while tmp_var:
            nodes.append(tmp_var)
            tmp_var = tmp_var.next_node

        sorted_nodes = sorted(nodes, key=lambda node: node.data)
        return sorted_nodes

    def sorted_insert(self, value):
        """New node at a given position.

        Args:
            value: value.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp_var = self.__head
            while (tmp_var.next_node is not None and
                    value >= tmp_var.next_node.data):
                tmp_var = tmp_var.next_node
            new_node.next_node = tmp_var.next_node
            tmp_var.next_node = new_node
