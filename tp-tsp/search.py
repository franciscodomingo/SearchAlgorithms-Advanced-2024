"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo, y los empates se resuelvan de forma aleatoria.
Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from problem import OptProblem
from random import choice
from time import time
import copy



class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)
        # actual es una lista de el orden de los nodos
        # el peso total del problema, es lo que queremos mejorar, arraca en -227334
        
        while True:
            #import pdb;pdb.set_trace()
            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan, con cada nodo
            diff = problem.val_diff(actual)
            #es un diccionario que tiene como key (n1,n2) dos nodos--> la accion, 
            # y como value el peso de ir de uno a otro
            
            
            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val ==
                        max(diff.values())]

            # Elegir una accion aleatoria, pues puede haber varias que tengan el máximo
            act = choice(max_acts)

            # Retornar si estamos en un optimo local
            # (diferencia de valor objetivo no positiva)
            if diff[act] <= 0:

                self.tour = actual
                self.value = value
                end = time()
                self.time = end-start
                return
            
            # Sino, nos movemos al sucesor
            else:
                actual = problem.result(actual, act) #no-ent
                value = value + diff[act]
                self.niters += 1


class HillClimbingReset(LocalSearch):
    """Algoritmo de ascension de colinas con reinicio aleatorio."""

    def solve(self, problem: OptProblem):
        # Starteamos el reloj
        start = time()

        # Elegimos una cantidad de iteraciones proporcional al tamaño del problema (a testear)
        amount_of_iterations = int(problem.G.number_of_nodes()/2)

        # Creamos una lista de instancias de HillClimbingReset de máximos locales
        list_of_solutions = []

    
        for i in range(amount_of_iterations):
            self_copy = copy.deepcopy(self)
            problem.init = problem.random_reset() #cambia el 
            HillClimbing.solve(self_copy, problem)
            list_of_solutions.append(self_copy)

        if len(list_of_solutions) == 0:
            return
        else:
            mejor_solucion = list_of_solutions[0]
            if len(list_of_solutions) > 1:
                for i in range(1, len(list_of_solutions)):
                    if list_of_solutions[i].value > mejor_solucion.value:
                        mejor_solucion = list_of_solutions[i]

            for i in list_of_solutions:
                self.niters += i.niters
            self.tour = mejor_solucion.tour
            self.value = mejor_solucion.value
            end = time()
            self.time = end-start
            return


class Cola():
    def __init__(self):
        self.lista = []

    def add(self, object):
        self.lista.append(object)

    def remove(self):
        if len(self.lista) != 0:
            self.lista.pop(0)

    def isEmpty(self):
        return len(self.lista) == 0


class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""

    def solve(self, problem: OptProblem):
        # Elegimos el límite de la memoria de corto plazo proporcional al tamaño del problema
        memory = int(problem.G.number_of_nodes()*0.3)
        lista_tabu = Cola()

        # Defimos el criterio de parada
        iteraciones_parada = problem.G.number_of_nodes()*40
        self.niters = iteraciones_parada

        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        mejor = problem.init
        mejor_value = problem.obj_val(problem.init)

        count = 0
        while count < iteraciones_parada:
            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            # Sacamos las acciones prohibidas
            if len(lista_tabu.lista) != 0:
                lista_a_eliminar = []
                for i in diff.keys():
                    if i in lista_tabu.lista:
                        lista_a_eliminar.append(i)
                for i in lista_a_eliminar:
                    del diff[i]

            if len(diff) == 0:
                lista_tabu.lista = []
                continue
            else:
                # Buscar las acciones que generan el mayor incremento de valor obj
                max_acts = [act for act, val in diff.items() if val ==
                            max(diff.values())]
                next = choice(max_acts)  # devuelve la key

                if max(diff.values()) > 0:
                    mejor = problem.result(actual, next)
                    mejor_value = problem.obj_val(mejor)

                # de cualquier forma me muevo
                actual = problem.result(actual, next)

                # Actualizo la lista tabu
                lista_tabu.add(next)
                while len(lista_tabu.lista) > memory:
                    lista_tabu.remove()

            count = count + 1

        self.tour = mejor
        self.value = mejor_value
        end = time()
        self.time = end-start
        return
