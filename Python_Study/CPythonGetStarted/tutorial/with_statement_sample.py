import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "a.text")


class Hello:
    def __enter__(self):
        print("memory allocation")
        return self

    def __call__(self):
        print(f"welcome {type(self).__name__} ")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{id(self)}: free")


if __name__ == "__main__":
    with open(FILE_PATH, "r") as f, Hello() as h:
        h()
        h()
        print(f.read())
