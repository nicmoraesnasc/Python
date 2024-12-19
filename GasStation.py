class GasStation:
    alcohol = 0
    gas = 0

    def set_alcohol(self, alcohol):
        self.alcohol = alcohol

    def set_gas(self, gas):
        self.gas = gas

    def get_alcohol_price(self) -> float:
        return self.alcohol * 1.90
        
    def get_gas_price(self) -> float:
        return self.gas * 2.50

    def get_alcohol_descount(self) -> float:
        alcohol_descount = 0
        if self.alcohol > 0:
            if self.alcohol <= 20:
                alcohol_descount = self.get_alcohol_price() - (self.alcohol * 0.03)
            else:
                alcohol_descount = self.get_alcohol_price() - (self.alcohol * 0.06)
        return alcohol_descount
            
    def get_gas_descount(self) -> float:
        gas_descount = 0
        if self.gas > 0:
            if self.alcohol <= 20:
                gas_descount = self.get_gas_price() - (self.gas * 0.04)
            else:
                gas_descount = self.get_gas_price() - (self.gas * 0.06)
        return gas_descount
    
gas_station = GasStation()

alcohol_or_gas = input("Digite A para Álcool ou G para Gasolina: ")

if alcohol_or_gas == "A" or alcohol_or_gas == "a":
    alcohol_amount = float(input("Quantidade de álcool desejado (litros): "))
    gas_station.set_alcohol(alcohol_amount)
    print("Valor do álcool: " + str(gas_station.get_alcohol_price()) + 
          "\nValor do álcool com os descontos: " + str(gas_station.get_alcohol_descount()))
elif alcohol_or_gas == "G" or alcohol_or_gas == "g":
    gas_amount = float(input("Quantidade de gasolina desejada (litros): "))
    gas_station.set_gas(gas_amount)
    print("Valor da gasolina: " + str(gas_station.get_gas_price()) + 
          "\nValor da gasolina com os descontos: " + str(gas_station.get_gas_descount()))
