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
                key = (particula.destino_x, particula.destino_y)
                value = (particula.origen_x, particula.origen_y, particula.distancia)
                if key in grafo:
                    grafo[key].append(value)
                else:
                    grafo[key] = [value]
        pprint(grafo, width=75)
        string = str(pformat(grafo, width=75, indent=1))
        return string