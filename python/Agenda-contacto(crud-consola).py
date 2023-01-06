import os

CARPETA = 'contactos/' #al poner toda la variable en mayusculas da a entender que es una constante osea que no se debe modificar su valor
EXTENCION = '.txt'

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria




def app ():
    #revisar si la carpeta existe
    crear_directorio()

    #Muestra el menu de opciones
    mostrar_menu()

    #Preguntar al usuario
    preguntar = True
    while preguntar:
        opcion = input("Seleccione una opcion: \r\n")
        opcion = int(opcion)

        #Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False

        elif opcion == 2:
            editar_contacto()
            preguntar = False

        elif opcion == 3:
            mostrar_contacto()
            preguntar = False

        elif opcion == 4:
            busca_contacto()
            preguntar = False

        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        else:
            print("Opcion no valida, Intente de nuevo")





def agregar_contacto():

    print("Escribe los datos para agregar el nuevo contacto")
    nombre_contacto = input("Nombre de contacto: \r\n")

    #revisar si el archivo ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)

    if not existe:

        #crea el archivo dentro de la carpeta, con el nombre que se ingrese y con la estencion que se tienen asiganda
        #Carpeta/nombre_contacto.EXTENCION  de esta froma seria la estructura
        with open(CARPETA + nombre_contacto + EXTENCION, 'w' ) as archivo:

            #Resto de los campos
            telefono_contacto = input('agrega el telefono \r\n')
            categoria_contacto = input('Categoria de Contacto \r\n')

            #instanciar la clase
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre:' + contacto.nombre + '\r\n')
            archivo.write('telefono:' + contacto.telefono + '\r\n')
            archivo.write('categoria:' + contacto.categoria + '\r\n')

            #Mostrar un mensaje de exito
            print('\r\n  CONTACTO CREADO CORRECTAMENTE  \r\n')


    else:
        print('\r\n ESE CONTACTO YA EXISTE \r\n')


    #reiniciar la App
    app()


def editar_contacto():
    print('Escribe el nombre del contacto a editar')
    nombre_anterior = input('Nombre del contacto que decea editar: \r\n')

    #revisar si el archivo si existe antes de editarlo
    existe = existe_contacto(nombre_anterior)

    if existe:
        with open(CARPETA + nombre_anterior + EXTENCION, 'w' ) as archivo:
            #Resto de los campos
            nombre_contacto = input("Agrega el nuevo Nombre: \r\n")
            telefono_contacto = input('agrega nuevo telefono: \r\n')
            categoria_contacto = input('Agrega nueva categoria: \r\n')

            #Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #escribir en el archivo
            archivo.write('Nombre:' + contacto.nombre + '\r\n')
            archivo.write('telefono:' + contacto.telefono + '\r\n')
            archivo.write('categoria:' + contacto.categoria + '\r\n')

            #Renombrar el archivo
            os.rename(CARPETA + nombre_anterior + EXTENCION, CARPETA + nombre_contacto + EXTENCION)

            #reiniciar Aplicacion
            app()
    else: 
        print('\r\n ESE CONTACTO NO EXISTE \r\n')
        app()


def mostrar_contacto():
    archivos = os.listdir(CARPETA)
    archivos_txt = [i for i in archivos if i.endswith(EXTENCION)]

    for archivos in archivos_txt:
        with open (CARPETA + archivos) as contacto:
            for linea in contacto:
                #Imprimer los contenidos
                print(linea.rstrip())
            #imprime un separador entre contactos
            print('\r\n')

    app()

def busca_contacto():
    nombre = input('Seleccione el nombre del contacto que deseas buscar \r\n')

    try:
        #buscador del contacto, de esta forma si el contacto no existe le mandara el mensaje de abajo y no arrojara un error
        with open(CARPETA + nombre + EXTENCION) as contacto:
            print('\r\n Información de contacto \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    
    #objesion si la funcion de arriba no es valida
    except IOError:
        print('\r\n EL CONTACTO NO EXISTE \r\n')
    
    #reiniciar app
    app()


def eliminar_contacto():
    nombre = input('Seleccione el nombre del contacto que deseas Eliminar \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENCION)
        print('\r\n ELIMINADO CORRECTAMENTE \r\n')

    except IOError:
        print('\r\n NO EXISTE ESE CONTACTO \r\n')
    

    app()


def mostrar_menu():
    print("seleccione el Menú de lo que desea hacer:")
    print("1) Agregar nuevo contacto")
    print("2) Editar contacto")
    print("3) Ver contactos")
    print("4) Buscar contacto")
    print("5) Eliminar contacto")
    

def crear_directorio():
    #si la carpeta no existe
    if not os.path.exists(CARPETA):
        #crear carpeta  la crea usando la libreria os
        os.makedirs(CARPETA)


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENCION)

app()