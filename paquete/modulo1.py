class persona:
    def __init__(self, nombre, apellido, domicilio, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.domicilio = domicilio
        self.edad = edad
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

def potencia(base, exponente):
    return base**exponente

def saludar(nombre):
    return f"hola gordo {nombre}"

paises = {"arg" : "argentina", "bra" : "brasil"}
