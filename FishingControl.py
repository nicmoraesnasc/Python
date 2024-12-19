class FishingControl:

    max_weight = 0
    fine = 0.0
    
    def set_max_weight(self, weight):
        self.max_weight = weight

    def set_fine(self, fine):
        self.fine = fine

    def get_excess_weight(self, fishing_weight):
        excess_weight = fishing_weight - self.max_weight

        if fishing_weight > self.max_weight:
            return excess_weight
        else:
            return 0.0

    def get_total_fine(self, fishing_weight):
        return (self.get_excess_weight(fishing_weight)) * self.fine
       

fishing_control = FishingControl()

fishing_weight = float(input("Quantidade pescada (kg): "))

fishing_control.set_max_weight(50.0)
fishing_control.set_fine(4.0)
print("Peso excedido: " + str(fishing_control.get_excess_weight(fishing_weight)) + " Kg")
print("Valor da multa: R$ " + str(fishing_control.get_total_fine(fishing_weight)))



            