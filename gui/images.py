from dataclasses import dataclass

@dataclass(init=True, repr=True)
class Data:
    path: str
    index: int

    def __iter__(self):
        yield self.path
        yield self.index
