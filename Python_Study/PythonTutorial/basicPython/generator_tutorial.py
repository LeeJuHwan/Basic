from collections import abc
import itertools


# next magic method override class
class NextPatternWordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(" ")

    def __next__(self):  # next need try - catch
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration("stop iteration")
        self._idx += 1
        return word

    def __repr__(self):
        return f"NextPatternWordSplitter{self._text}"

    def __len__(self):
        return len(self._text)


# Iterator magic method class
class IteratorPatternWordSplit:
    def __init__(self, text):
        self._text = text.split(" ")

    def __iter__(self):
        for word in self._text:
            yield word

    def __repr__(self):
        return f"IteratorPatternWordSplit{self._text}"

    def __len__(self):
        return len(self._text)


def generator_func():
    print("START")
    yield "A break point"
    print("CONTINUE")
    yield "B break point"
    print("END")


# iterable type check
if __name__ == "__main__":
    # a = "ABCDEFGHIJKMLNOPQRSTUVWXYZ"

    # i = iter(a)

    # while i:
    #     try:
    #         print(next(i), end=" ")
    #     except StopIteration:
    #         break
    # print()
    # print(hasattr(a, "__iter__"))
    # print(isinstance(a, abc.Iterable))

    # --------------- iterable class practice -------------------
    np_word_split = NextPatternWordSplitter("Life is too short, you need python")

    print(
        " ".join(
            repr(next(np_word_split)).replace("'", "")
            for _ in range(len(np_word_split))
        )
    )
    print(isinstance(np_word_split, abc.Iterable))
    print(hasattr(np_word_split, "__iter__"))

    it_word_split = IteratorPatternWordSplit("Life is too short, you need python")

    it = iter(it_word_split)
    print(" ".join(repr(next(it)).replace("'", "") for _ in range(len(it_word_split))))
    print(isinstance(it_word_split, abc.Iterable))
    print(hasattr(it_word_split, "__iter__"))

    # -------------- generator func practice --------------
    tmp = iter(generator_func())

    for g in generator_func():
        print(g)

    tmp2 = (x * 3 for x in generator_func())
    # for i in tmp2:
    #     print(i)

    counter = itertools.count(1, 1)  # 자연수 생성
    # print(next(counter))

    tw = itertools.takewhile(lambda x: x < 1000, counter)
    # for i in tw:
    #     print(i)

    ff = itertools.filterfalse(lambda x: x < 3, list(range(1, 6)))  # not x < 3
    # for i in ff:
    #     print(i)

    acc = itertools.accumulate([x for x in range(1, 101)])  # 1... 100 -> 1 ~ 5050
    # for i in acc:
    #     print(i)

    chaining = itertools.chain("AB", range(1, 6))  # ['A', 'B', 1, 2, 3, 4, 5]
    # print(list(chaining))

    chaining2 = itertools.chain(enumerate("ABCDE"))  # [(0, 'A'), (1, 'B'),
    # print(list(chaining2))

    pd = itertools.product(
        "ABCDE", repeat=2
    )  # 경우의 수 [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'),
    # print(list(pd))

    gb = itertools.groupby("AAABBCCCCDDEE")  # A: ['A', 'A', 'A'], B: ['B', 'B']

    # for i, j in gb:
    #     print(f"{i}: {list(j)}")
