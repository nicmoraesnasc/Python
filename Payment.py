class Payment:

    payment_per_hour = 0
    hours_worked = 0

    def set_payment_per_hour(self, payment_per_hour):
        self.payment_per_hour = payment_per_hour

    def set_hours_worked(self, hours_worked):
        self.hours_worked = hours_worked

    def get_gross_wage(self):
        return self.payment_per_hour * self.hours_worked

    def get_income_tax(self):
        return self.get_gross_wage() * 0.11
    
    def get_inss(self):
        return self.get_gross_wage() * 0.08
    
    def get_syndicate(self):
        return self.get_gross_wage() * 0.05
    
    def get_net_wage(self):
        return (self.get_gross_wage() - self.get_income_tax() - self.get_inss() - self.get_syndicate())


payment = Payment()

payment.set_payment_per_hour(31.0)
payment.set_hours_worked(176.0)

print("Salário bruto: R$ " + str(payment.get_gross_wage()))
print("Imposto de renda: R$ " + str(payment.get_income_tax()))
print("INSS: R$ " + str(payment.get_inss()))
print("Sindicato: R$ " + str(payment.get_syndicate()))
print("Salário líquido: R$ " + str(payment.get_net_wage()))
