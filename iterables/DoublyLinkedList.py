from .node import Node
from typing import List

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.current = None

    @staticmethod
    def list_to_doubly_linked_list(data: List) -> "DoublyLinkedList":
        linked_list = DoublyLinkedList()
        for item in data:
            linked_list.append(item)

        linked_list.current = linked_list.head
        return linked_list
    
    def append(self, data) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def get_current(self) -> Node:
        return self.current

    def go_back(self) -> bool:
        current = self.get_current()
        if current and current.prev:
            self.current = current.prev
            return True

        print("Reached the beginning of the list or current is None.")
        return False

    def go_forward(self) -> bool:
        current = self.get_current()
        if current and current.next:
            self.current = current.next
            return True

        print("Reached the end of the list or current is None.")
        return False

    def __iter__(self) -> "DoublyLinkedList":
        self.current = self.head  # Reset current to head for iteration
        return self

    def __next__(self) -> Node:
        if not self.current:
            raise StopIteration

        current_data = self.current.data
        self.current = self.current.next
        return current_data

    def __repr__(self) -> str:
        return f'Current node: {self.current}, Head: {self.head}, Tail: {self.tail}'
