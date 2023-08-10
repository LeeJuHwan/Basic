import time


def decorator_outer(func):
    def decorator_inner(*args):
        # start time
        start = time.perf_counter()

        # business logic
        result = func(*args)

        # end time
        end = time.perf_counter()

        name = func.__name__
        print(f"args: {args}")
        args_str = ",".join(repr(arg) for arg in args)

        print(f"{end - start:.5f}s {name}({args_str}) ->  {result} ")

        return result

    return decorator_inner


@decorator_outer
def sleep_func(seconds):
    time.sleep(seconds)


@decorator_outer
def sum_func(*numbers):
    return sum(numbers)


if __name__ == "__main__":
    print(f"free variable: {sum_func.__code__.co_freevars}")
    print(sleep_func(2))
    print(sum_func(1, 2, 3, 4, 5, 6, 7))
