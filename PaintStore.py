import math

class CanType:
    liters = 0
    cost = 0

    def __init__(self, liters=0, cost=0):
        self.liters = liters
        self.cost = cost

    def __str__(self):
        return "liters[" + str(self.liters) + "] cost[" + str(self.cost) + "]"
    

    def set_liters(self, liters):
        self.liters = liters

    def set_cost(self, cost):
        self.cost = cost

class PaintStore:
    number_of_can_types = 0

    size_painted_area = 0
    area_per_liter = 0
    can_types = []

    def add_type(self, can_type:CanType):
        self.can_types.append(can_type)

    def get_can_types(self):
        return self.can_types

    # def set_number_of_can_types(self, number_of_types):
    #     if number_of_types < 1:
    #         self.number_of_can_types = 1
    #     else:
    #         self.number_of_can_types = number_of_types

    #         self.liters_per_can = [0] * self.number_of_can_types
    #         self.can_cost = [0] * self.number_of_can_types

    # def set_area_per_liter(self, area_per_liter):
    #     self.area_per_liter = area_per_liter

    # def set_size_painted_area(self, size_painted_area):
    #     self.size_painted_area = size_painted_area

    # def set_liters_per_can(self, can_type, liters_per_can):
    #     if can_type > self.number_of_can_types or can_type < 1:
    #         return
    #     else:
    #         self.liters_per_can[can_type - 1] = liters_per_can

    # def set_can_cost(self, can_type, can_cost):
    #     if can_type > self.number_of_can_types or can_type < 1:
    #         return
    #     else:
    #         self.can_cost[can_type - 1] = can_cost

    # def get_total_amount_paint(self):
    #     return self.size_painted_area / self.area_per_liter
    
    # def get_total_amount_cans(self, can_type):
    #     if can_type > self.number_of_can_types or can_type < 1:
    #         return
    #     else:
    #         return math.ceil(self.get_total_amount_paint() / self.liters_per_can[can_type - 1])
    
    # def get_total_cost_paint(self, can_type):
    #     if can_type > self.number_of_can_types or can_type < 1:
    #         return
    #     else:
    #         return self.get_total_amount_cans(can_type) * self.can_cost[can_type - 1]
        
    # def get_order_can_types(self):
    #     unordered_list = []
    #     for can_type in range(self.number_of_can_types):

    

        
    # # def get_all_can_types(self):

    
paintstore = PaintStore()

paintstore.add_type(CanType(liters=18.0, cost=80.0))
paintstore.add_type(CanType(liters=3.6, cost=25.0))
paintstore.add_type(CanType(liters=10.0, cost=45.0))
paintstore.add_type(CanType(liters=5.0, cost=30.0))

for can_type in paintstore.get_can_types():
    print(can_type)

# can_type = int(input("1 - Apenas latas de 18L\n2 - Apenas latas de 3,6L\n3 - Ambas latas\n>"))

# paintstore.set_area_per_liter(6)
# paintstore.set_number_of_can_types(2)

# paintstore.set_can_cost(1, 80.0)
# paintstore.set_can_cost(2, 25.0)

# paintstore.set_liters_per_can(1, 18)
# paintstore.set_liters_per_can(2, 3.6)

# print(paintstore.get_order_can_types())

# size_area = float(input("Tamanho da área a ser pintada (m²): "))
# paintstore.set_size_painted_area(size_area)

# print("Quantidade total de latas de tinta: " + str(paintstore.get_total_amount_cans(can_type)))
# print("Valor total da tinta: R$" + str(paintstore.get_total_cost_paint(can_type)))
    
