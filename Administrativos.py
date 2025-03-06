from Persona import Persona

class Administrativo(Persona):
    def __init__(self, nombre, edad, direccion, cargo, fecha_vinculacion):
        super().__init__(nombre, edad, direccion)
        self.__cargo = cargo
        self.__fecha_vinculacion = fecha_vinculacion
        
    def get_cargo(self):
        return self.__cargo
    
    def set_cargo(self, cargo):
        self.__cargo=cargo    
        
    def get_fecha_vinculacion(self):
        return self.__fecha_vinculacion

    def set_fecha_vinculacion(self, fecha_vinculacion):
        self.__fecha_vinculacion=fecha_vinculacion
    
    def __str__(self):
        return f"Los datos del administrativo son los siguientes:\n{super().__str__()}\nSu cargo es: {self.get_cargo()}\nSu fecha de vinculación es: {self.get_fecha_vinculacion()}"    