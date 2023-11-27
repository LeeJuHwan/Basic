from typing import List

string_array = ["a", "b", "c", "e", "d", "e", "f", "c"]


def find_duplicate(string_array: List[str]) -> str:
    """
    문자열 배열에서 중복 값 반환
    """
    result = []
    index_dictionary = {}

    for data in string_array:
        if index_dictionary.get(data):
            result.append(data)

        index_dictionary[data] = True

    return result


if __name__ == "__main__":
    print(find_duplicate(string_array))
