from types import MappingProxyType
from dis import dis


source = (
    ("k1", "val1"),
    ("k1", "val2"),
    ("k2", "val3"),
    ("k2", "val4"),
    ("k2", "val5"),
)

dict1 = {}

for k, v in source:
    dict1.setdefault(k, []).append(v)

# frozen dict
const_dict_frozen = MappingProxyType(dict1)


print(f"일반 딕셔너리: {id(dict1)}")
print(f"이뮤터블 딕셔너리: {id(const_dict_frozen)}")
print(type(const_dict_frozen))  # type(mappingproxy)

# const_dict_frozen["key2"] = "value2" -> TypeError: 'mappingproxy' object does not support item assignment

# frozenset
garbage_data = {"a", "b", "c", "d", "e"}
const_garbage_data = frozenset(garbage_data)

print(type(const_garbage_data))  # type -> frozenset


# 선언문 성능 확인
print(dis("{10}"))  # load const - build_set - return_vlaue
print(dis("set(10)"))  # load_name - load_const - call_function - return value
