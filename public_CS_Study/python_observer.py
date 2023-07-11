class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def unregister(self, observer):
        self.__observers.remove(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

    def __str__(self):
        return type(self).__name__


class Observer:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(f"{self} -> {args[0]} From {subject}")

    def __str__(self):
        return type(self).__name__


class Observer1(Observer):
    def __init__(self, subject):
        super().__init__(subject)


class Observer2(Observer):
    def __init__(self, subject):
        super().__init__(subject)


if __name__ == "__main__":
    subject = Subject()
    observer1 = Observer1(subject)
    observer2 = Observer2(subject)
    subject.notifyAll("notification")
    subject.unregister(observer2)
    subject.notifyAll("notification")
