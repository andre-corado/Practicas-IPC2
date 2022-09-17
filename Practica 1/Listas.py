import os
import webbrowser
from datetime import datetime

class Pan:
    def __init__(self, salchicha, chorizo, salami, longaniza, costilla):
        self.salchicha = salchicha
        self.chorizo = chorizo
        self.salami = salami
        self.longaniza = longaniza
        self.costilla = costilla
        contador = 0
        if salchicha:
            contador += 2
        if chorizo:
            contador += 3
        if salami:
            contador += 1.5
        if longaniza:
            contador += 4
        if costilla:
            contador += 6
        self.tiempoPreparacion = contador


class Orden:
    def __init__(self, nombre, cantidadShucos, tiempoDeEspera):
        self.nombre = nombre
        self.cantidadShucos = cantidadShucos
        self.tiempoDeOrden = 0
        self.tiempoDeEspera = tiempoDeEspera
        self.panes = ListaEnlazada()

    def sumarTiempo(self, tiempoPan):
        self.tiempoDeOrden += tiempoPan


class Nodo:
    def __init__(self, dato: Orden = None, siguiente=None):
        self.orden = dato
        self.siguiente = siguiente


class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def insertar(self, pan):
        if self.primero is None:
            self.primero = Nodo(dato=pan)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = Nodo(dato=pan)


class Cola:
    def __init__(self):
        self.primero = None
        self.tiempoDeEsperaAcumulado = 0

    def push(self, orden):
        if self.primero is None:
            self.primero = Nodo(dato=orden)
            self.tiempoDeEsperaAcumulado += self.primero.orden.tiempoDeOrden
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = Nodo(dato=orden)
            self.tiempoDeEsperaAcumulado += actual.siguiente.orden.tiempoDeOrden
        self.graficar(datetime.now().strftime("%Y-%m-%d_a_las_%H.%M.%S"), 1)

    def pop(self):
        if self.primero is not None:
            primerNodo = self.primero
            self.primero = self.primero.siguiente
            primerNodo.siguiente = None
            self.tiempoDeEsperaAcumulado -= primerNodo.orden.tiempoDeOrden
            if self.primero:
                self.actualizarTiemposdeEspera()
            self.graficar(datetime.now().strftime("%Y-%m-%d_a_las_%H.%M.%S"), 2)
            return primerNodo
        else:
            return None

    def print(self):
        if self.primero is None:
            print('No existen órdenes aún.\nPresione Enter para regresar.')
            input()
            return
        j = 1
        actual = self.primero
        while actual:
            print('___________________________________________________________________________________')
            print('\n\n\t\t\tORDEN NO. ' + str(j))
            orden = actual.orden
            print(f'\nNombre: {orden.nombre}\t\t\tCantidad de Shucos:{str(orden.cantidadShucos)}')
            i = 1
            actualPan = orden.panes.primero
            while actualPan:
                pan = actualPan.orden
                print('----------------------------------------------')
                print('\t\tSHUCO NO. ' + str(i))
                if pan.salchicha:
                    print('■ Salchicha')
                if pan.chorizo:
                    print('■ Chorizo')
                if pan.salami:
                    print('■ Salami')
                if pan.longaniza:
                    print('■ Longaniza')
                if pan.costilla:
                    print('■ Costilla')
                i += 1
                actualPan = actualPan.siguiente
            print(f'\nTiempo de Preparación:{orden.tiempoDeOrden}\tTiempo de Espera:{orden.tiempoDeEspera}')
            j += 1
            actual = actual.siguiente
        print('___________________________________________________________________________________')
        print('\n\nPresione Enter para regresar.')

    def actualizarTiemposdeEspera(self):
        self.primero.orden.tiempoDeEspera = 0
        actual = self.primero
        contador = 0
        while actual.siguiente is not None:
            contador += actual.orden.tiempoDeOrden
            actual.siguiente.orden.tiempoDeEspera = contador
            actual = actual.siguiente

    def graficar(self, nombre, item):
        actual = self.primero
        graphviz = 'digraph Patron{ \n node[shape =box, width = 6, height = 2]; \n ranksep = 0 \n subgraph Cluster_A{ \n label = "' + 'Órdenes de Shucos' + '"   \n fontcolor ="black" \n fontsize = 41 \n bgcolor ="#c6e2e9" \n'
        noOrden = 1
        if actual is None:
            graphviz += 'node' + str(noOrden) + '[label = "'+ 'No hay órdenes por el momento ' + '" fontcolor = "black" fontsize = 20 fillcolor = "#a7bed3" style = filled]; \n'

        while actual:
            orden = actual.orden
            graphviz += 'node' + str(noOrden) + '[label = "' + 'Orden ' + str(noOrden) + '\n________________________________________________________________\n' + '\nCliente: ' + orden.nombre + '\n\n Cantidad de Shucos: ' + str(orden.cantidadShucos) + ' | Tiempo de Espera: ' + str(
                orden.tiempoDeEspera) + 'min | Tiempo de Preparación: ' + str(orden.tiempoDeOrden)+ 'min' '" fontcolor = "black" fontsize = 20 fillcolor = "#a7bed3" style = filled]; \n'
            actual = actual.siguiente
            noOrden += 1
        m = 1
        a = 2
        for h in range(noOrden - 2):
            graphviz += 'node{}->node{} \n'.format(m, a)
            m += 1
            a += 1

        graphviz += '} \n}'

        document = 'ArchivoAuxiliarGraphViz' + '.txt'
        with open(document, 'w') as grafica:
            grafica.write(graphviz)

        if item == 1:
            jpg = 'OrdenAgregada_' + nombre + '.jpg'
            os.system("dot.exe -Tjpg " + document + " -o " + jpg)
            webbrowser.open(jpg)
        elif item == 2:
            jpg = 'OrdenEntregada_' + nombre + '.jpg'
            os.system("dot.exe -Tjpg " + document + " -o " + jpg)
            webbrowser.open(jpg)
