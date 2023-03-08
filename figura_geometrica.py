from codecs import latin_1_decode


class FiguraGeometrica():
    def __init__(self,lado) -> None:
        self.lado = lado

    def __str__(self) -> str:
        return self.lado

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado) -> None:
        super().__init__(lado)

    def perimetro(self):
        return 2*self.lado
    
    def area(self):
        return pow(self.lado,2)

    def __str__(self) -> str:
        return "Cuadrado de lados {}".format(super().__str__())

c1=Cuadrado(20)

print(c1)
print(c1.area())
print(c1.perimetro())