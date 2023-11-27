from typing import List


def get_alphabet_dict() -> List[str]:
    lower_first_alphabet: int = ord("a")
    lower_last_alphabet: int = ord("z")

    alphabet_list: List[str] = {chr(i): False for i in range(lower_first_alphabet, lower_last_alphabet+1)}

    return alphabet_list


def find_does_not_exists_alphabet(string: str):
    """
    알파벳 문자를 한글자만 제외하고 모두 포함하는 문자열을 받아 빠진 문자 하나를 반환하는 함수를 작성하라
    """
    alpahbet_dict: List[str] = get_alphabet_dict()

    for word in string:
        alpahbet_dict[word] = word

    for alphabet, result in alpahbet_dict.items():
        if not result:
            return alphabet


if __name__ == "__main__":
    test = "the quick brown box jupms over a lazy dog"

    print(find_does_not_exists_alphabet(test))
