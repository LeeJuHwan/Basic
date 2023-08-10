def copyright(func):
    def wrapper():
        print("@copyright python")
        print(f"name: {func.__name__}\temoji: ", end="")
        func()
        print()

    return wrapper


@copyright
def smile():
    print("😀")


@copyright
def angry():
    print("🤯")


@copyright
def love():
    print("😍")


@copyright
def scarey():
    print("😱")


@copyright
def wear_a_mask():
    print("😷")


@copyright
def zip_your_mouth():
    print("🤐")


@copyright
def wutang_signs_up():
    print("👐")


@copyright
def clap():
    print("👏")


if __name__ == "__main__":
    smile()
    angry()
    love()
    scarey()
    clap()
    wutang_signs_up()
    zip_your_mouth()
    wear_a_mask()
