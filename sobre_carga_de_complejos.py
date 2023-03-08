import re


class Complejo:
    #Ejemplo de sobrecarga de operadores
    def __init__(self,real,imaginaria) -> None:
        self.real = real
        self.imaginaria = imaginaria

    def __str__(self) -> str:
        return ("{}+{}i".format(self.real, self.imaginaria))

    def __add__(self,otro):
        return Complejo(self.real+otro.real, self.imaginaria+otro.imaginaria)

    def __sub__(self,otro):
        return Complejo(self.real+otro.real, self.imaginaria-otro.imaginaria)
    
    def __mul__(self,otro): #Multiplica numeros reales e imaginarios
        n_real=(self.real*otro.real)-(self.imaginaria*otro.imaginaria)
        n_imaginaria= (otro.imaginaria*self.real) +(otro.real*self.imaginaria)
        return Complejo(n_real,n_imaginaria)

n1=Complejo(2,6);
n2=Complejo(3,5)
n3=n1*n2
print(n3)