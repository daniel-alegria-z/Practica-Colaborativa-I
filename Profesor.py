from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, direccion, telefono, materia, titulacion, horario, salario,):
        super().__init__(nombre, edad, direccion)
        self.__telefono = telefono
        self.__materia = materia
        self.__titulacion = titulacion
        self.__horario = horario
        self.__salario = salario

    def get_materia(self):
        return self.__materia

    def set_materia(self, materia):
        self.__materia = materia

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_titulacion(self):
        return self.__titulacion

    def set_titulacion(self, titulacion):
        self.__titulacion = titulacion

    def get_horario(self):
        return self.__horario

    def set_horario(self, horario):
        self.__horario = horario
    
    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        self.__salario = salario

    def _str_(self):
        return f"Los datos del profesor son los siguientes:\n{super()._str_()}\nTeléfono: {self.get_telefono()}\nMateria: {self.get_materia()}\nTitulación: {self.get_titulacion()}\nHorario: {self.get_horario()}\nsalario: {self.get_salario()}"
    