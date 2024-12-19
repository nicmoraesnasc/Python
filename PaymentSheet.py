class PaymentSheet:

    payment = 0

    def set_payment(self, payment):
        self.payment = payment

    def get_readjustment(self) -> float:
        if self.payment > 0:
            if self.payment <= 280.00:
                self.payment += self.payment * 0.20
                return self.payment
            elif self.payment > 280.00 and self.payment <= 700.00:
                self.payment += self.payment * 0.15
                return self.payment
            elif self.payment > 700.00 and self.payment <= 1500.00:
                self.payment += self.payment * 0.10
                return self.payment
            else:
                self.payment += self.payment * 0.05
                return self.payment
        else:
            return 0

    def get_increase_value(self) -> float:
        return "%.2f" % (self.payment - payment)
        
    def get_percentage(self):
        percentage = 0
        if self.payment > 0:
            if self.payment <= 280.00:
                percentage = 20
                return percentage
            elif self.payment > 280.00 and self.payment <= 700.00:
                percentage = 15
                return percentage
            elif self.payment > 700.00 and self.payment <= 1500.00:
                percentage = 10
                return percentage
            else:
                percentage = 5
                return percentage
        else:
            return 0

payment_sheet = PaymentSheet()

payment = float(input("Digite o salário: "))

payment_sheet.set_payment(payment)
percentage = payment_sheet.get_percentage()
readjustment = payment_sheet.get_readjustment()
increase_value = payment_sheet.get_increase_value()

print("Salário antes do reajuste: R$" + str(payment))
print("Percentual do reajuste: " + str(percentage) + "%" )
print("Valor do aumento: R$" + str(increase_value))
print("Salário reajustado: R$" + str(readjustment))

