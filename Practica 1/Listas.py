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

    def pop(self):
        if self.primero is not None:
            primerNodo = self.primero
            self.primero = self.primero.siguiente
            primerNodo.siguiente = None
            self.tiempoDeEsperaAcumulado -= primerNodo.orden.tiempoDeOrden
            if self.primero:
                self.actualizarTiemposdeEspera()
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
