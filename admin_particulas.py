from particulas import Particula
import json
from pprint import pprint, pformat

class Administradora():
    def __init__(self):
        self.__particulas = []
        self.__grafo = {}

    def agregar_inicio(self, particula: Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula: Particula):
        self.__particulas.append(particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(str(particula) + '\n' for particula in self.__particulas)

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=3)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula)for particula in lista]
            return 1
        except:
            return 0

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0
        return self
    
    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration
    
    def sort_by_id(self):
        particulas = self.__particulas
        particulas.sort(key=lambda particula: particula.id)

    def sort_by_distancia(self):
        particulas = self.__particulas
        particulas.sort(key=lambda particula: particula.distancia, reverse=True)
    
    def sort_by_velocidad(self):
        particulas = self.__particulas
        particulas.sort(key=lambda particula: particula.velocidad)

    def mostrarG(self):
        grafo = self.__grafo
        if len(grafo) == 0:
            for particula in self.__particulas:
                key_origen = (particula.origen_x, particula.origen_y)
                key_destino = (particula.destino_x, particula.destino_y)
                value_origen = ((particula.destino_x, particula.destino_y), particula.distancia)
                value_destino = ((particula.origen_x, particula.origen_y), particula.distancia)
                if key_origen in grafo:
                    grafo[key_origen].append(value_origen)
                else:
                    grafo[key_origen] = [value_origen]
                if key_destino in grafo:
                    grafo[key_destino].append(value_destino)
                else:
                    grafo[key_destino] = [value_destino]
        pprint(grafo, width=75)
        string = str(pformat(grafo, width=75, indent=1))
        return string

    def busqueda_profundidad(self, origen_x, origen_y):
        grafo = self.__grafo
        origen = (origen_x, origen_y)
        vectorVisitados = []
        vectorRecorrido = []
        pila = []
        if grafo:
            vectorVisitados.append(origen)
            pila.append(origen)

            while pila:
                vertice = pila[-1]
                vectorRecorrido.append(vertice)
                pila.pop()
                for key, value in grafo[vertice]:
                    if key not in vectorVisitados:
                        vectorVisitados.append(key)
                        pila.append(key)
            pprint(vectorRecorrido)
            return 1
        else:          
            return 0

    def busqueda_Amplitud(self, origen_x, origen_y):
        grafo = self.__grafo
        origen = (origen_x, origen_y)
        vectorVisitados = []
        vectorRecorrido = []
        cola = []
        if grafo:
            vectorVisitados.append(origen)
            cola.append(origen)

            while cola:
                vertice = cola[0]
                vectorRecorrido.append(vertice)
                cola.pop(0)
                for key, value in grafo[vertice]:
                    if key not in vectorVisitados:
                        vectorVisitados.append(key)
                        cola.append(key)
            pprint(vectorRecorrido)
            return 1
        else:
            return 0