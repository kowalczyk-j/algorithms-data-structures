import typing
from abc import ABC, abstractmethod
from typing import List

from typing_extensions import Protocol

C = typing.TypeVar("C", bound="Comparable")


class Comparable(Protocol):
    @abstractmethod
    def __lt__(self: C, other: C) -> bool:
        pass

    @abstractmethod
    def __gt__(self: C, other: C) -> bool:
        pass


class AbstractHeap(ABC):
    def __init__(self, num_children: int) -> None:
        pass

    def __len__(self) -> int:
        return len(self.get_raw_data())

    @abstractmethod
    def peek(self) -> C:
        """Get the topmost element without changing the heap."""

    @abstractmethod
    def push(self, value: C):
        """Add an element to the heap."""

    @abstractmethod
    def pop(self) -> C:
        """Remove the topmost element from the heap and return it."""

    @abstractmethod
    def get_raw_data(self) -> List[C]:
        """Get the underlying data storage."""


class Heap(AbstractHeap):

    def __init__(self, num_children: int) -> None:
        if num_children < 2:
            raise ValueError("Minimum number of children is 2.")
        self._a = num_children
        self._list = []

    def __len__(self) -> int:
        return len(self._list)

    def __str__(self) -> str:
        return self._print()

    def peek(self) -> C:
        if len(self):
            return self._list[0]

    def push(self, value: C):
        self._list.append(value)
        self._shift_up(len(self) - 1)

    def _shift_up(self, idx: int):
        item = self._list[idx]
        parent_idx = (idx - 1) // self._a

        while self._list[parent_idx] > item and idx > 0:
            self._list[idx] = self._list[parent_idx]
            idx = parent_idx
            parent_idx = (idx - 1) // self._a

        self._list[idx] = item

    def pop(self) -> C:
        if len(self) == 0:
            raise ValueError("Cannot remove element from empty heap.")
        root = self._list[0]
        self._list[0] = self._list[-1]
        self._list.pop(-1)
        if len(self) > 1:
            self._shift_down(0)
        return root

    def _shift_down(self, idx):
        while idx * self._a <= len(self):
            child_idx = self._find_min_child(idx)
            if child_idx == -1:
                break
            if self._list[idx] > self._list[child_idx]:
                self._list[idx], self._list[child_idx] = self._list[child_idx], self._list[idx]
            idx = child_idx

    def _find_min_child(self, idx):
        min_child = self._list[idx]
        min_child_idx = -1
        i = 1
        while self._a * idx + i < len(self) and i <= self._a:
            if self._list[self._a * idx + i] < min_child:
                min_child = self._list[self._a * idx + i]
                min_child_idx = self._a * idx + i
            i += 1

        return min_child_idx

    def _print(self, root=0, depth=1) -> str:
        result_string = ""

        leftmost_child = root * self._a + 1
        children = list(range(
            leftmost_child,
            min(len(self), leftmost_child + self._a)
        ))

        left_children = children[:self._a // 2][::-1]
        right_children = children[self._a // 2:][::-1]

        for child in right_children:
            result_string += self._print(child, depth + 4)

        result_string += " " * depth + repr(self._list[root]) + '\n'

        for child in left_children:
            result_string += self._print(child, depth + 4)

        return result_string

    def get_raw_data(self) -> List[C]:
        return self._list


class BinaryHeap(Heap):
    def __init__(self):
        super().__init__(2)


class TernaryHeap(Heap):
    def __init__(self):
        super().__init__(3)


class QuarternaryHeap(Heap):
    def __init__(self):
        super().__init__(4)


if __name__ == "__main__":
    heap = TernaryHeap()
    nums = [3, 6, 8, 5, 12, 64, 2, 22, 10, 7, 4, 4]
    for num in nums:
        heap.push(num)
    print(heap)
