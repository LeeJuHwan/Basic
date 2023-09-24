import dis
import instaviz

co = compile("b+1", "test.py", mode="eval")
print(f"compile object: {co}")
print(f"compile byte code: {co.co_code}")
print("reverse assembly > word code:")
dis.dis(co.co_code)


# def example():
#     a = 1
#     b = a + 1
#     return b


# instaviz.show(example)
