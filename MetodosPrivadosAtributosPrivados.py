from multiprocessing import reduction


class Ejemplo():
    def __init__(self) -> None:
        self.__oculto="Me encuentro oculto en la clase"
    
    def publico(self):
        return "Soy un metodo publico"

    def __privado(self):
        return "Soy un metodo privado"
    
    def get_oculto(self):
        return self.__oculto
    
    def set_oculto(self):
        self.__oculto=self.__privado()

ej1=Ejemplo()

print(ej1.publico)
print(ej1.get_oculto)
# print(ej1.set_oculto())
print(ej1._Ejemplo__privado()) #---> Forma de acceder a un metodo privado
print(ej1._Ejemplo__oculto) #--> Forma de acceder a un atributo privado
# -- Al intentar acceder a metodos/atributos privados de la forma tradicional saltará el error --
# print(ej1.__privado) #ERROR: AttributeError: 'Ejemplo' object has no attribute '__privado'
# print(ej1.__oculto) #ERROR: AttributeError: 'Ejemplo' object has no attribute '__oculto'. Did you mean: 'get_oculto'?