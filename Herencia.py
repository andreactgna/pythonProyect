class Padre():

    def __init__(self,cabello="negro",ojos="azules") -> None:
        self.cabello = cabello
        self.ojos= ojos

    def conducir_coche(self):
        print("La persona sabe conducir")

    def __str__(self) -> str:
        return "{} {}".format(self.cabello,self.ojos)

class Hijo(Padre):

    def __init__(self, cabello, ojos,cara) -> None:
        super().__init__(cabello, ojos)
        self.cara=cara

    def conducir_moto(self):
        print("La persona sabe conducir motos")
    
    def __str__(self) -> str:
        return super().__str__()+" {}".format(self.cara)

persona=Hijo("negro","marrones","alargada")

print(persona)
persona.conducir_coche()
persona.conducir_moto()