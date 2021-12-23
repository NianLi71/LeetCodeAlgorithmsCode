from typing import TypeVar, Generic, List
T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

num_discs: int = 4
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(num_discs, 0, -1):
    tower_a.push(i)

# print(tower_a)

def show_towers() -> None:
    print(tower_a)
    print(tower_b)
    print(tower_c)
    print()

def hanoi(src: Stack[int], des: Stack[int], temp: Stack[int], num_discs_to_move: int) -> None:
    show_towers()
    if num_discs_to_move == 1:
        des.push(src.pop())
    else:
        hanoi(src, temp, des, num_discs_to_move - 1)
        hanoi(src, des, temp, 1)
        hanoi(temp, des, src, num_discs_to_move - 1)

if __name__ == '__main__':
    hanoi(tower_a, tower_c, tower_b, num_discs)
    show_towers()