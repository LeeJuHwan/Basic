from typing import List, Tuple


def set_up() -> Tuple[List]:
    array1 = [i for i in range(1, 6)]
    array2 = [i for i in range(0, 9, 2)]

    return array1, array2


def intersection(array1: List[int], array2: List[int]) -> List[int]:
    """
    두 배열의 교집합 반환
    단, 복잡도는 O(N)으로 설계 할 것
    """
    base_array: List[int] = array1
    iteration_array: List[int] = array2

    if len(array1) > len(array2):
        base_array = array2
        iteration_array = array1

    index_dictionary = {data: True for data in iteration_array}  # O(N)

    result = [data for data in base_array if index_dictionary.get(data)]  # O(N)

    return result


if __name__ == "__main__":
    arr1, arr2 = set_up()
    print(intersection(arr1, arr2))
