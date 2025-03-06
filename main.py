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