class Vector:
    def __init__(self, *args):
        """
        벡터 생성
        e.g: Vector(5, 10)
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """벡터 정보"""
        return f"Vector({self._x}, {self._y})"

    def __add__(self, cls_instance):
        """벡터 클래스 간 더하기 연산"""
        return Vector(self._x + cls_instance._x, self._y + cls_instance._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))


if __name__ == "__main__":
    v1 = Vector(5, 7)
    v2 = Vector(23, 35)
    v3 = Vector()

    print(v1, v2, v3)
    print(v1 + v2)

    print(v1 * 3)
    print(bool(v3), bool(v2), bool(v1))
