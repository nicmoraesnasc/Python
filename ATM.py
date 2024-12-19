class ATM:

    withdrawal_amount = 0
    one_dollar = 1
    five_dollars = 5
    ten_dollars = 10
    fifty_dollars = 50
    hundred_dollars = 100

    one_dollar_quantity = 0
    five_dollars_quantity = 0
    ten_dollars_quantity = 0
    fifty_dollars_quantity = 0
    hundred_dollars_quantity = 0

    def set_withdrawal_amount(self, withdrawal_amount):
        self.withdrawal_amount = withdrawal_amount

    def get_bill_values(self) -> list[int]:

        rest = self.withdrawal_amount

        if self.withdrawal_amount >= 10 and self.withdrawal_amount <= 600:

            if rest >= self.hundred_dollars:
                self.hundred_dollars_quantity = rest // self.hundred_dollars
                rest = rest % self.hundred_dollars
            if rest >= self.fifty_dollars:
                self.fifty_dollars_quantity = rest // self.fifty_dollars
                rest = rest % self.fifty_dollars
            if rest >= self.ten_dollars:
                self.ten_dollars_quantity = rest // self.ten_dollars
                rest = rest % self.ten_dollars 
            if rest >= self.five_dollars:
                self.five_dollars_quantity = rest // self.five_dollars
                rest = rest % self.five_dollars
            if rest >= self.one_dollar:
                self.one_dollar_quantity = rest // self.one_dollar
                rest = rest % self.one_dollar
        else:
            print("Valor mínimo: R$10,00 \nValor máximo: R$600,00")

        return [self.hundred_dollars_quantity, self.fifty_dollars_quantity,
                self.ten_dollars_quantity, self.five_dollars_quantity, self.one_dollar_quantity]
                

atm = ATM()

amount = int(input("Valor: "))

withdrawal_amount = atm.set_withdrawal_amount(amount)

bill_values = atm.get_bill_values()

if bill_values[0] > 0:
    print("Notas de 100 dólares: " + str(bill_values[0]))
if bill_values[1] > 0:
    print("Notas de 50 dólares: " + str(bill_values[1]))
if bill_values[2] > 0:
    print("Notas de 10 dólares: " + str(bill_values[2]))
if bill_values[3] > 0:
    print("Notas de 5 dólares: " + str(bill_values[3]))
if bill_values[4] > 0:
    print("Notas de 1 dólar: " + str(bill_values[4]))