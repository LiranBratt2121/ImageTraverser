import pyperclip

from os import listdir
from typing import List
from dataclasses import dataclass

from iterables.DoublyLinkedList import DoublyLinkedList


@dataclass(init=True, repr=True)
class Data:
    path: str
    index: int

    def __iter__(self):
        yield self.path
        yield self.index


class Images:
    def __init__(self, data_or_dir: List[Data] | str) -> None:
        is_str = isinstance(data_or_dir, str)
        is_data_list = isinstance(data_or_dir, List) and not any(not isinstance(item, Data) for item in data_or_dir)

        if not (is_str or is_data_list):
            raise TypeError("data_or_dir should be either a list of Data objects or a directory path")

        self.paths = DoublyLinkedList.list_to_doubly_linked_list(data_or_dir if is_data_list else
                                                                 [Data(path=images_dir, index=i) for i, images_dir in enumerate(listdir(data_or_dir), start=1)])

    def forward(self) -> bool:
        return self.paths.go_forward()

    def back(self) -> bool:
        return self.paths.go_back()

    def get_current(self) -> Data:
        return self.paths.get_current().data

    def copy_path_to_clipboard(self) -> None:
        path = self.get_current().path
        pyperclip.copy(path)
        print(f"Copied {path} to clipboard.")