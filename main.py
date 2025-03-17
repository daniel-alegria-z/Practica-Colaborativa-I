from Profesor import Profesor
from Administrativos import Administrativo
from Estudiante import Estudiante

lista_profesor = []
lista_administrativo = []
lista_estudiante = []


def registrar_administrativo():
    print('Se va a registrar un administrativo')
    nombre = input('\nIngresar el nombre completo del administrativo: ')
    direccion = input('Ingresar la dirección: ')
    edad = input('Ingresar la edad: ')
    cargo = input('Ingresar el cargo: ')
    fecha_vinculacion = input('Ingresar la fecha de vinculación (DD/MM/AA): ')
    
    administrativo = Administrativo(nombre, edad, direccion, cargo, fecha_vinculacion)
    lista_administrativo.append(administrativo)
    print('\nAdministrativo guardado con éxito\n')
    
def mostrar_administrativo():
    num = 1
    if len(lista_administrativo) == 0:
        print("\nNo hay administrativos en la lista.\n\n")
    else:
        print('\nSe va a mostrar un listado de administrativos:\n')
        for administrativo in lista_administrativo:
            print(f'#{num}.')
            num += 1
            print(administrativo, "\n")
        print("Administrativos listados en su totalidad con éxito.\n")
        
def actualizar_administrativo():
    nombre_actualizar = input("Ingrese el nombre del administrativo a actualizar: ")
    for administrativo in lista_administrativo:
        if administrativo.get_nombre() == nombre_actualizar:
            print(f"\nAdministrativo encontrado. {administrativo}")
            administrativo.set_nombre(input("\nIngrese el nuevo nombre completo del administrativo: "))
            administrativo.set_direccion(input("Ingrese la nueva dirección: "))
            administrativo.set_edad(input("Ingrese la nueva edad: "))
            administrativo.set_cargo(input("Ingrese el nuevo cargo: "))
            administrativo.set_fecha_vinculacion(input("Ingrese la nueva fecha de vinculación (DD/MM/AA): "))
            print(f"\nAdministrativo '{nombre_actualizar}' actualizado exitosamente!\n")
            return
    print(f"\nNo se encontró al administrativo con nombre '{nombre_actualizar}'\n")
    
def eliminar_administrativo():
    nombre_eliminar = input("Ingrese el nombre del administrativo a eliminar: ")
    for administrativo in lista_administrativo:
        if administrativo.get_nombre() == nombre_eliminar:
            lista_administrativo.remove(administrativo)
            print(f"\nAdministrativo '{nombre_eliminar}' eliminado exitosamente!\n")
            return
    print(f"\nNo se encontró al administrativo con nombre '{nombre_eliminar}'\n")    
    

def registrar_profesor():
    print('Se va a registrar un profesor')
    nombre = input('\nIngresar el nombre completo del profesor: ')
    direccion = input('Ingresar la dirección: ')
    edad = input('Ingresar la edad: ')
    telefono = input('Ingresar el teléfono: ')
    materia = input('Ingresar la materia que imparte: ')
    titulacion = input('Ingresar la titulación: ')
    horario = input('Ingresar el horario de clases: ')
    salario = input('Ingresar el salario: ')

    profesor = Profesor(nombre, edad, direccion, telefono, materia, titulacion, horario, salario)
    lista_profesor.append(profesor)  
    print('\nProfesor guardado con éxito\n')

def mostrar_profesor():
    num = 1    
    if len(lista_profesor) == 0:
        print("\nNo hay profesores en la lista.\n\n")
    else:
        print('\nSe va a mostrar un listado de profesores:\n')
        for profesor in lista_profesor:
            print(f'#{num}.')
            num += 1
            print(profesor, "\n")
        print("Profesores listados en su totalidad con éxito.\n")

def actualizar_profesor():
    nombre_a_actualizar = input("Ingrese el nombre del profesor a actualizar: ")
    for profesor in lista_profesor:
        if profesor.get_nombre() == nombre_a_actualizar:
            print(f"\nProfesor encontrado. {profesor}")
            profesor.set_nombre(input("\nIngrese el nuevo nombre completo del profesor: "))
            profesor.set_direccion(input("Ingrese la nueva dirección: "))
            profesor.set_edad(input("Ingrese la nueva edad: "))
            profesor.set_telefono(input("Ingrese el nuevo teléfono: "))
            profesor.set_materia(input("Ingrese la nueva materia: "))
            profesor.set_titulacion(input("Ingrese la nueva titulación: "))
            profesor.set_horario(input("Ingrese el nuevo horario: "))
            profesor.set_salario(input("Ingrese el nuevo salario: "))
            print(f"\nProfesor '{nombre_a_actualizar}' actualizado exitosamente!\n")
            return
    print(f"\nNo se encontró al profesor con nombre '{nombre_a_actualizar}'\n")

def eliminar_profesor():
    nombre_a_eliminar = input("Ingrese el nombre del profesor a eliminar: ")
    for profesor in lista_profesor:
        if profesor.get_nombre() == nombre_a_eliminar:
            lista_profesor.remove(profesor)
            print(f"\nProfesor '{nombre_a_eliminar}' eliminado exitosamente!\n")
            return
    print(f"\nNo se encontró al profesor con nombre '{nombre_a_eliminar}'\n")

def registrar_estudiante():
    print('Se va a registrar un estudiante')
    name = input('\nIngresar el nombre completo del estudiante: ')
    address = input('Ingrese el dirección: ')
    age = input('Ingrese la edad: ')
    course = input('Ingresar el curso: ')

    estudiante = Estudiante(name, age, address, course) 
    lista_estudiante.append(estudiante) 
    print('\nEstudiante guardado con éxito\n')

def mostrar_estudiante():
    num = 1    
    if len(lista_estudiante) == 0:
        print("\nNo hay estudiantes en la lista.\n\n")
    else:
        print('\nSe va a mostrar un listado de estudiantes:\n')
        for estudiante in lista_estudiante:
            print(f'#{num}.')
            num += 1
            print(estudiante, "\n")
        print("Estudiantes listados en su totalidad con éxito.\n")

def actualizar_estudiante():
    nombre_actualizar = input("Ingrese el nombre completo del estudiante a actualizar: ")
    for estudiante in lista_estudiante:
        if estudiante.get_nombre() == nombre_actualizar:
            print(f"\nEstudiante encontrado. {estudiante}")
            estudiante.set_nombre(input("\nIngrese el nuevo nombre completo: "))
            estudiante.set_direccion(input("Ingrese la nueva dirección: "))
            estudiante.set_edad(input("Ingrese la nueva edad: "))
            estudiante.set_curso(input("Ingrese el nuevo curso: "))
            print(f"\nEstudiante '{nombre_actualizar}' actualizado exitosamente!\n")
            return
    print(f"\nNo se encontró al estudiante con nombre '{nombre_actualizar}'\n")

def eliminar_estudiante():
    nombre_eliminar = input("Ingrese el nombre completo del estudiante a eliminar: ")
    for estudiante in lista_estudiante:
        if estudiante.get_nombre() == nombre_eliminar:
            lista_estudiante.remove(estudiante)
            print(f"\nEstudiante '{nombre_eliminar}' eliminado exitosamente!\n")
            return
    print(f"\nNo se encontró al estudiante con nombre '{nombre_eliminar}'\n")

def menu_root():
    while True:
        print('::: MENU USUARIO ROOT :::')
        print("""    1. Registrar administrativo 
    2. Consultar listado de administrativos
    3. Actualizar datos de administrativo
    4. Eliminar un administrativo
    5. Volver al Menú Principal""")
        op = input('Ingresa la opcion que desee ejecutar: ')
        
        if op == '1':
            registrar_administrativo()
        elif op == '2':
            mostrar_administrativo()
        elif op == '3':
            actualizar_administrativo()
        elif op == '4':
            eliminar_administrativo()
        elif op == '5':
            print('\nVolviendo al menú principal...\n')
            return
        else:
            print('Opción inválida')
            
            
            
def menu_administrador():
    while True:
        print('::: MENU ADMINISTRADOR :::')
        print("""    1. Registrar profesor 
    2. Consultar listado de profesores
    3. Actualizar datos de profesor
    4. Eliminar profesores
     
    5. Registrar estudiante 
    6. Consultar listado de estudiantes
    7. Actualizar datos de estudiante
    8. Eliminar un estudiante
     
    9. Volver al Menú Principal""")
        op = input('Ingresa la opcion que desee ejecutar: ')
        
        if op == '1':
            registrar_profesor()
        elif op == '2':
            mostrar_profesor()
        elif op == '3':
            actualizar_profesor()
        elif op == '4':
            eliminar_profesor()
        elif op == '5':
            registrar_estudiante()
        elif op == '6':
            mostrar_estudiante()
        elif op == '7':
            actualizar_estudiante()
        elif op == '8':
            eliminar_estudiante()
        elif op == '9':
            print('\nVolviendo al menú principal...\n')
            return 
        else:
            print('Opción inválida')

def menu_profesor():
    while True:
        print('::: MENU PROFESOR :::')
        print("""    1. Registrar estudiante 
    2. Consultar listado de estudiantes
    3. Actualizar datos de estudiante
    4. Eliminar un estudiante
    5. Volver al Menú Principal""")
        op = input('Ingresa la opcion que desee ejecutar: ')
        
        if op == '1':
            registrar_estudiante()
        elif op == '2':
            mostrar_estudiante()
        elif op == '3':
            actualizar_estudiante()
        elif op == '4':
            eliminar_estudiante()
        elif op == '5':
            print('\nVolviendo al menú principal...\n')
            return
        else:
            print('Opción inválida')

def menu_estudiante():
    while True:
        print('::: MENU ESTUDIANTE :::')
        print("""    1. Consultar Listado
    2. Volver al Menú Principal""")
        op = input('Ingresa la opcion que desee ejecutar: ')
        
        if op == '1':
            mostrar_estudiante()
        elif op == '2':
            print('\nVolviendo al menú principal...\n')
            return  # Regresa al menú principal
        else:
            print('Opción inválida')

def menu_principal():
    while True:
        print('::: MENU PRINCIPAL :::')
        print("""    0. Root
    1. Administrador
    2. Profesor
    3. Estudiante
    4. Salir""")
        
        op = input('Ingresa la opción que desee ejecutar: ')
        
        if op == '0':
            menu_root()
        elif op == '1':
            menu_administrador()
        elif op == '2':
            menu_profesor()
        elif op == '3':
            menu_estudiante()
        elif op == '4':
            print('\nSaliendo del sistema...')
            exit()
        else:
            print('Opción inválida')


menu_principal()