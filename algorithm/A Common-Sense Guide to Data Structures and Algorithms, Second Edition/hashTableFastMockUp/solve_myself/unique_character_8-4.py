def find_one_character_in_string(string: str) -> str:
    """문자열에서 첫 번째 중복되지 않는 문자를 반환하는 함수를 작성하라"""

    duplicate_character_dict = {}

    for char in string:

        if duplicate_character_dict.get(char):
            duplicate_character_dict[char] += 1
        else:
            duplicate_character_dict[char] = 1

    for char, i in duplicate_character_dict.items():
        if i == 1:
            return char


if __name__ == "__main__":
    test = "minimum"
    print(find_one_character_in_string(test))
