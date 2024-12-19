class Triangle:

    triangle_side1 = 0
    triangle_side2 = 0
    triangle_side3 = 0

    def set_triangle_sides(self, triangle_side1, triangle_side2, triangle_side3):
        self.triangle_side1 = triangle_side1
        self.triangle_side2 = triangle_side2
        self.triangle_side3 = triangle_side3

    def is_triangle(self):
        if (self.triangle_side2 - self.triangle_side3) < self.triangle_side1 < self.triangle_side2 + self.triangle_side3:
            return True
        else:
            return False

    def get_triangle_type(self) -> float:
        if self.is_triangle():
            if self.triangle_side1 == self.triangle_side2 == self.triangle_side3:
                print("Triangulo equilátero")
            elif self.triangle_side1 == self.triangle_side2 or self.triangle_side1 == self.triangle_side3 or self.triangle_side2 == self.triangle_side3:
                print("Triângulo isóceles")
            elif self.triangle_side1 != self.triangle_side2 != self.triangle_side3:
                print("Triângulo escaleno")
        else:
            print("Não é um triângulo")

                    
triangle = Triangle()

side1 = float(input("Digite o tamanho do 1º lado de um triângulo: "))
side2 = float(input("Digite o valor do 2º lado de um triângulo: "))
side3 = float(input("Digite o valor do 3º lado de um triângulo: "))

triangle.set_triangle_sides(side1, side2, side3)

triangle.get_triangle_type()


