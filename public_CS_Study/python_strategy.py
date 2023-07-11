class PaymentStrategy:
    def pay(self, amount):
        pass


class KakaoCardStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} paid using KakaoCard")


class LunaCardStrategy(PaymentStrategy):
    def pay(self, amount):
        print(f"{amount} paid using LunaCard")


class Payment:
    def __init__(self, strategy):
        self._strategy = strategy

    def pay_amount(self, amount):
        return self._strategy.pay(amount)


pay_will_amount = 400

payment = Payment(KakaoCardStrategy())
payment.pay_amount(pay_will_amount)
payment = Payment(LunaCardStrategy())
payment.pay_amount(pay_will_amount)
