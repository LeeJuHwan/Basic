from dataclasses import dataclass
from typing import List, Dict, Tuple, Callable, Union, Optional, TypeVar, Generic
from typing_extensions import TypedDict

integer: int = 42
string: str = "hello world"
floating_of_number: float = 42.0
boolean: bool = True

list_variable: List[int] = [1, 2, 3]
tuple_variable: Tuple[int, ...] = (1, 2, 3)

dictionary: Dict[str, str] = {"python": "we need"}

union_variable: Union[str, int] = 0 or "1"


ARM = TypeVar("ARM", int, float, str)
HEAD = TypeVar("HEAD", int, float, str)
T = TypeVar("T", int, float, str)
K = TypeVar("K", int, float, str)


def add(x: int, y: int) -> int:
    return x + y


def function_params(func: Callable[[int, int], int]) -> int:
    return func(1, 2)


class IsPythonic:
    def hello_python(self) -> int:
        return 42


hello_word: IsPythonic = IsPythonic()
hi_python: Optional["IsPythonic"] = IsPythonic()


def hi(obj: IsPythonic) -> int:
    return obj.hello_python()


class Point(TypedDict):
    x: int
    y: float
    z: str


point: Point = {
    "x": 42,
    "y": 42.0,
    "z": "42",
}


def test(x: T) -> T:
    print(x)
    return x


@dataclass
class Robot(Generic[T, K]):  # generic: arm -> ARM이 어떤 타입의 역할을 수행 할지 결정하게 함
    arm: T
    head: K

    def decode(self):
        bbb: Optional[T] = None
        print(type(bbb))
        print(type(T))
        pass


class Siri(Generic[T, K], Robot[T, K]):
    pass


if __name__ == "__main__":
    robot1 = Robot[str, int]("123412", 1234123)  # 타입의 역할을 명시 해줌으로, ARM의 타입은 int로 결정됨
    robot2 = Robot[int, int](12341124122, 1234122313)
    robot3 = Robot[float, int](11242.123412, 1234123123)

    siri1 = Siri[str, int]("123412", 1234123)  # 타입의 역할을 명시 해줌으로, ARM의 타입은 int로 결정됨
    siri2 = Siri[int, int](12341124122, 1234122313)
    siri3 = Siri[float, int](11242.123412, 1234123123)

    test(898)
