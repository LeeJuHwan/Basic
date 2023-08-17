from dataclasses import dataclass
from typing import List, Optional, Generic, TypeVar

T = TypeVar("T")


@dataclass
class Node(Generic[T]):
    item: T
    next: Optional["Node"] = None


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional["Node"] = None

    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        cur_node: Node = self.head
        count: int = 1

        while cur_node.next is not None:
            cur_node = cur_node.next
            count += 1
        return count

    def __str__(self) -> str:
        result: str = ""

        if self.head is None:
            return result
        cur_node: Node = self.head
        result += f"{cur_node.item}"

        while cur_node.next is not None:
            cur_node = cur_node.next
            result += f", {cur_node.item}"
        return result


class Stack(LinkedList, Generic[T]):
    def push(self, item):
        node: Node[T] = Node(item)
        if self.head is None:
            self.head = node
            return
        cur_node = self.head

        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = node

    def pop(self):
        if self.head is None:
            raise ValueError("stack is empty")
        else:
            cur_node = self.head

        if cur_node.next is None:
            self.head = None
            return cur_node.item

        while cur_node.next.next is not None:
            cur_node: Node = cur_node.next

        result = cur_node.next
        cur_node.next = None
        return result.item


class Queue(Generic[T], LinkedList[T]):
    def enqueue(self, item: T) -> None:
        node: Node[T] = Node(item)
        if self.head is None:
            self.head = node
            return
        cur_node = self.head

        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = node

    def dequeue(self) -> T:
        if self.head is None:
            raise ValueError("queue is empty")
        
        cur_node = self.head
        if cur_node.next is None:
            self.head = None
            return cur_node.item

        result = cur_node.item
        self.head = cur_node.next
        return result


if __name__ == "__main__":
    # stack: Stack[int] = Stack()

    # stack.push(42)
    # stack.push(12)
    # stack.push(4)

    # stack.pop()
    # print(stack)
    # stack.push(6)
    # stack.pop()
    # print(stack)
    # print(stack.length)
    # print(stack.head.next)
    # stack.pop()
    # stack.pop()
    # print(stack)

    queue = Queue[int]()
    queue.enqueue(42)
    queue.enqueue(1)
    queue.enqueue(12)
    queue.enqueue(16)

    queue.dequeue()
    queue.dequeue()
    print(queue)
