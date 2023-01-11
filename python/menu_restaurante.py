import os

#Variables constantes
CARPETA = 'Restaurante/'
EXTENCION = '.txt'

class menu():
    def __init__(self, plato, contenido, precio):
        self.plato = plato
        self.contenido = contenido
        self.precio = precio


def app ():

    #Crear carpeta
    crear_directorio()

    #Mostrar el menu
    mostrar_menu()

    preguntar = True
    while preguntar:
        opcion = input("Seleccione una opcion: \r\n")
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_plato()
            preguntar = False

        elif opcion == 2:
            editar_plato()
            preguntar = False

        elif opcion == 3:
            ver_menu()
            preguntar = False

        elif opcion == 4:
            buscar_plato()
            preguntar = False

        elif opcion == 5:
            eliminar_plato()
            preguntar = False
        else:
            print("Opcion no valida, Intente de nuevo")

def agregar_plato():
    print("\r\n Escribe los datos para agregar el nuevo plato al menu \r\n")
    nombre_plato = input("Nombre del Plato: \r\n")

    #revisar si existe:
    existe = existe_plato(nombre_plato)

    if not existe:
        with open(CARPETA + nombre_plato + EXTENCION, 'w' ) as archivo:
            contenido_plato = input('¿Que contiene el plato? \r\n')
            precio_plato = input('¿Que precio tiene el plato? \r\n')

            #instanciar la clase
            plato = menu(nombre_plato, contenido_plato, precio_plato)

            #Escribir en el archivo
            archivo.write('PLATO:  ' + plato.plato + '\r\n')
            archivo.write('CONTENIDO:  ' + plato.contenido + '\r\n')
            archivo.write('PRECIO:  ' + plato.precio + '\r\n')

            #Mostrar un mensaje de exito
            print('\r\n  PLATO CREADO CORRECTAMENTE  \r\n')

def editar_plato():
    
    #enunciar lo que se va a buscar
    nombre_anterior = input('Nombre del plato que decea editar: \r\n')

    #revisar si el archivo si existe antes de editarlo
    existe = existe_plato(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENCION, 'w' ) as archivo:
            #Resto de los campos
            nombre_plato = input("Agrega el nuevo Nombre del plato: \r\n")
            contenido_plato = input('agrega el contenido del plato: \r\n')
            precio_plato = input('precio del plato: \r\n')

            #Instanciar
            plato = menu(nombre_plato, contenido_plato, precio_plato)

            #escribir en el archivo
            archivo.write('NOMBRE:' + plato.plato + '\r\n')
            archivo.write('CONTENIDO:' + plato.contenido + '\r\n')
            archivo.write('PRECIO:' + plato.precio + '\r\n')

            #Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENCION, CARPETA + nombre_plato+ EXTENCION)

            #mensaje de exito
            print('\r\n PLaTO MODIFICADO CORRECTAMENTE \r\n')
            #reiniciar Aplicacion
            app()
    else: 
        print('\r\n ESE CONTACTO NO EXISTE \r\n')
        app()

def ver_menu():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENCION)]

    for archivos in archivos_txt:
        with open (CARPETA + archivos) as menu:
            for linea in menu:
                #Imprimer los contenidos
                print(linea.rstrip())
            #imprime un separador entre contactos
            print('\r\n')

    app()

def buscar_plato():
    plato = input('Seleccione el plato que deseas buscar \r\n')

    try:
        with open(CARPETA + plato + EXTENCION) as plato:
            print('\r\n Información de Plato \r\n')
            for linea in plato:
                print(linea.rstrip())
            print('\r\n')
    
    #objesion si la funcion de arriba no es valida
    except IOError:
        print('\r\n EL PLATO NO EXISTE \r\n')
        app()

def eliminar_plato():
    plato = input('Seleccione el nombre del plato que deseas Eliminar \r\n')

    try:
        os.remove(CARPETA + plato + EXTENCION)
        print('\r\n ELIMINADO CORRECTAMENTE \r\n')

    except IOError:
        print('\r\n NO EXISTE ESE CONTACTO \r\n')
    

    app()

def crear_directorio():
    #si la carpeta no existe
    if not os.path.exists(CARPETA):
        #crear carpeta  la crea usando la libreria os
        os.makedirs(CARPETA)

def mostrar_menu():

    print("seleccione el Menú de lo que desea hacer:")
    print("1) Agregar nuevo plato")
    print("2) Editar plato")
    print("3) Ver menu")
    print("4) Buscar plato")
    print("5) Eliminar plato")

def existe_plato(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENCION)

app()