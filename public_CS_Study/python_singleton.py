class Singleton:
    def __new__(cls):
        print("NEW: ", hasattr(cls, "instance"))
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
            print("CLS constructor:", id(cls.instance))
        else:
            print("exists instance:", id(cls.instance))
        return cls.instance


base_singleton = Singleton()
new_singleton = Singleton()

assert base_singleton == new_singleton
print("BASE SINGLETON: ", id(base_singleton))
print("NEW SINGLETON: ", id(new_singleton))
base_singleton.DTO = "base singleton to new singleton"
print("DATA TRANSFER FROM BASE:", new_singleton.DTO)
new_singleton.DTO = "new singleton to new singleton"
print("DATA TRANSFER FROM NEW:", base_singleton.DTO)
