from Listas import *
import os


def printMenu():
    print('\t\t ÓRDENES DE SHUKOS.\n\tELIJA UNA OPCIÓN:\n')
    print('1.\tAgregar Orden\n2.\tEliminar Orden\n3.\tVer Datos del Estudiante\n4.\tVisualizar Cola\n5.\tSalir')

# Solicita la Orden al Usuario
def crearOrden():
    os.system('cls')
    salchicha = chorizo = salami = longaniza = costilla = False
    print('Ingrese el nombre del cliente:')
    nombre = input().upper()
    while not nombre:
        print('\nIngrese un nombre:')
        nombre = input().upper()
        if nombre:
            break
    print('\nIngrese la cantidad de shucos de la orden:')
    cantidadShucos = 0
    while True:
        try:
            cantidadShucos = int(input())
            if (cantidadShucos is None) or cantidadShucos < 1:
                print('ERROR: Debe de ingresar un número entero mayor a 0.')
                continue
            else:
                break
        except:
            print('ERROR: Debe de ingresar un número entero mayor a 0.')
            continue
    #Se inicia la orden con los respectivos datos.
    orden = Orden(nombre, cantidadShucos, cola.tiempoDeEsperaAcumulado)
    for i in range(1, cantidadShucos + 1):
        print('\n\n\t\tINGREDIENTES: Shuco No. '+ str(i) + '\nPara confirmar un ingrediente ingrese \'S\' o \'s\'\nDe no desearlo'
              ' puede ingresar cualquier otro dato o ninguno.')
        print("\n¿Desea el shuco con SALCHICHA?")
        respuesta = input().capitalize()
        if respuesta == 'S':
            salchicha = True
            print("\n¿Desea el shuco con CHORIZO?")
        respuesta = input().capitalize()
        if respuesta == 'S':
            chorizo = True
        print("\n¿Desea el shuco con SALAMI?")
        respuesta = input().capitalize()
        if respuesta == 'S':
            salami = True
        print("\n¿Desea el shuco con LONGANIZA?")
        respuesta = input().capitalize()
        if respuesta == 'S':
            longaniza = True
        print("\n¿Desea el shuco con COSTILLA?")
        respuesta = input().capitalize()
        if respuesta == 'S':
            costilla = True
        #Se añade cada pan a la orden
        pan = Pan(salchicha, chorizo, salami, longaniza, costilla)
        orden.panes.insertar(pan)
        orden.sumarTiempo(pan.tiempoPreparacion)
    os.system('cls')
    print('\tORDEN AÑADIDA EXITOSAMENTE\nPresione Enter para regresar.')
    input()
    return orden


if __name__ == '__main__':
    cola = Cola()
    menu = ''
    while True:
        os.system('cls')
        printMenu()
        menu = input()
        # Agregar Orden
        if menu == '1':
            os.system('cls')
            orden = crearOrden()
            cola.push(orden)

        # Eliminar Orden
        if menu == '2':
            os.system('cls')
            ordenEliminada = cola.pop()
            if ordenEliminada is not None:
                print('Orden Eliminada.\nPresione Enter para regresar.')
                input()
            else:
                print('\t ERROR: No existen ordenes para eliminar.\nPresione Enter para regresar.')
                input()
        # Visualizar mis Datos
        if menu == '3':
            os.system('cls')
            print('Nombre:\t Sergio André Lima Corado\t\tCarné:\t202100154')
            print('Curso:\t Introducción a la Programación y Computación 2\nSección:\tN\nPresione Enter para regresar.')
            input()
        # Visualizar cola en consola
        if menu == '4':
            os.system('cls')
            cola.print()
            input()
        # Salir
        if menu == '5':
            break
