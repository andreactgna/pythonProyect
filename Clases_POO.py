class Pelicula:

    #Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelocuala:",self.titulo)

    def __str__(self):
        return"{} ({})".format(self.titulo,self.lanzamiento)

class Catalogo:

    #Esta lista cotendrá objetos de la clase Pelicula
    peliculas = []

    def __init__(self,peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):# p será un objeto pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)#Print toma por defecto str(p)

class Estudiante:
    #class variable
    escuela = "RAMIRO DE MAEZTU"

    def __init__(self, nombre, rol) -> None:
        self.nombre = nombre
        self.rol = rol

class Libro:
    def __init__(self, paginas) -> None:
         self.paginas= paginas

    def __add__(self,otro):
        return self.paginas+otro.paginas

    def __sub__(self,otro):
        return self.paginas-otro.paginas

    def __eq__(self,otro):
        return self.paginas==otro.paginas    


li= Libro(100)
l2= Libro(200)

print("Total paginas ",li-l2)

# e1=Estudiante("Ana", "Estudiante")
# e2=Estudiante("Pedro", "Estudiante")

# print(e1.nombre,e1.rol,e1.escuela)
# print(e2.nombre,e2.rol,e2.escuela)

# # e1.escuela="GRAN CAPITAL" --> cambia el estudiante especifico.
# # Estudiante.escuela="GRAN CAPITAL" -->  cambia la variable de la clase y todos los que apunten ahí cambian.

# print(e1.nombre,e1.rol,e1.escuela)
# print(e2.nombre,e2.rol,e2.escuela)

# p1 = Pelicula("El Padrino",175,1972)
# p2 = Pelicula("abc",120,1990)
# #Añado un lista con una pelicula desde el principio
# c=Catalogo([p1,p2])
# c.mostrar()
# c.agregar(Pelicula("El Padrino: Parte 2",202,1974))
# c.mostrar()

# #Inicializas el Catalogo con una lista vacia
# otro=Catalogo()
# otro.agregar(p1)
# otro.agregar(p2)