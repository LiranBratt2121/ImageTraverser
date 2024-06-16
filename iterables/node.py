from typing import Any

class Node:
    def __init__(self, data: Any):
        self.data = data
        self.prev = None
        self.next = None