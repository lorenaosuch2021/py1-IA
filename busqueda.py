##
# Proy#1: Resolucion de problemas con busqueda
#
# En este proyecto exploramos busqueda de costo uniforme,
# busqueda informada, y distintas heuristicas para mejorar 
# la busqueda.
#
# Tambien miramos a varios problemas tipicos y usamos A* para 
# resolverlos
#
#

 
# probablmente te sirva heapq
import heapq
import time
from math import *


######
# UTILITARIOS
######

# Esto te sirve para calcular el tiempo
# Fuente: http://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python
def current_time() :
    return int(round(time.time()*1000))


# Funcion a utilizarse para generar estados sucesores del estado INICIO
#def sucesores(camino_original, meta):
	## Implemente su funcion aqui
	
	# Devuelve una lista de caminos a tus soluciones
	#return []


# NO CAMBIAR FIRMA DE ESTE METODO (el calificador automatico lo va a usar)
#
# Dado una lista de estados (el camino al ultimo estado) esta funcion usa
# el ultimo estado para generar TODOS los posibles estados sucesores y retorna
# una lista de CAMINOS sucesores.
#
# Ej (8-puzzle):
#
# Si tu estado original era:
#  
#   [[1,2,3],[4,5,6],[7,8,0]]
# 
# y tu camino original era:
#
#  [ [[1,2,3],[4,5,6],[7,8,0]] ]
#
# posibles estados sucesores son:
#
#  [[1,2,3],[4,5,0],[7,8,6]] 
#   y
#  [[1,2,3],[4,5,6],[7,0,8]] 
#
# Entonces esta funcion devuelve:
#
# 
#   [
#   [
#   [[1,2,3],[4,5,6],[7,8,0]],   [[1,2,3],[4,5,0],[7,8,6]] 
#   ],  
#   [
#   [[1,2,3],[4,5,0],[7,8,6]],   [[1,2,3],[4,5,6],[7,0,8]] 
#   ]
#   ]
#
def sucesores(camino_original) :

    # INGRESA TU CODIGO AQUI

    # Devuelve una lista de caminos a tus soluciones
    
    # Obtiene la posición del espacio en blanco (0)
    fila_vacia, col_vacia = None, None
    for fila in range(len(camino_original)):
        if 0 in camino_original[fila]:
            fila_vacia, col_vacia = fila, camino_original[fila].index(0)
            break
    print("fila_vacia: ", fila_vacia)
    print("col_vacia: ", col_vacia)
    # Genera los movimientos posibles (arriba, abajo, izquierda, derecha)
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Genera los estados sucesores
    sucesores = []
    for fila, col in movimientos:
        nueva_fila_vacia, nueva_col_vacia = fila_vacia + fila, col_vacia + col
        if 0 <= nueva_fila_vacia < len(camino_original) and 0 <= nueva_col_vacia < len(camino_original[0]):
            nuevo_estado = [fila.copy() for fila in camino_original]  # Clona el estado actual
            nuevo_estado[fila_vacia][col_vacia], nuevo_estado[nueva_fila_vacia][nueva_col_vacia] = nuevo_estado[nueva_fila_vacia][nueva_col_vacia], nuevo_estado[fila_vacia][col_vacia]
            print("nuevo estado: ", nuevo_estado)
            sucesores.append(nuevo_estado)
    
    # Devuelve una lista de caminos a los sucesores
    sucesores.append(camino_original)
    for suc in sucesores:
        print("contenido de sucesores: ", suc)
    sucesores.reverse()
    resultado = []
    # Itera sobre la lista original para generar las sublistas
    for i in range(len(sucesores) - 1):
        sublista = [sucesores[i], sucesores[i + 1]]
        resultado.append(sublista)
    
    return resultado
######
# RESOLVEDOR GENERAL DE PROBLEMAS
######

# NO CAMBIAR FIRMA DE ESTE METODO (el calificador automatico lo va a usar)
#
# Esto hace una busqueda de costo uniforme
#
# Utiliza la funcion succesores_fn para generar estados sucesores del estado INICIO
# y hace un recorrido BFS por el arbol de sucesores para encontrar una solucion 
# optima.
#
# max_prof es la profundidad maxima de pasos para llegar a la solucion
# evita que corra para siempre el algoritmo si no esta encontrado una solucion.
#
# Recuerda: el arbol de soluciones es un arbol de CAMINOS no de estados, y requerda
# usar un conjunto (set en python) para evitar visitar el mismo estado 2 veces (sino
# entraras a un bucle infinito)
#
def uc_bfs(inicio, meta, sucesores_fn=sucesores, costo_camino_fn=len, max_prof=1000) :
     
    # TU CODIGO AQUI - Devuelve el numero de estados que exploraste
    # y una lista de estados indicando los pasos a la solucion (el camino a la solucion)


     num_estados_recorridos = 0
     solucion= None
     return (num_estados_recorridos, solucion)

    


# NO CAMBIAR FIRMA DE ESTE METODO (el calificador automatico lo va a usar)
#
# Implementa el algoritmo A*
#
# heuristica_fn se refiere a la funcion que calcula la heuristica (debe recibir un camino)
# sucesores_fn se refiere a la funcion que dado un camnio genera los sucesores
# max_prof es la profunidad maxima del camino antes de darnos por vencidos
#
def a_estrella(inicio, meta, heuristica_fn, sucesores_fn=sucesores, costo_camino_fn=len, max_prof=1000) :

     # TU CODIGO AQUI - cambialo para que haga A* y reporte 
     # cuantos estados recorrio y el camino mas optimo que resuelva este
     # problema (Nota: puede resolver CUALQUIER PROBLEMA no solo 8-Puzzle)
     
     # Pistas: te servira heapq y set

     num_estados_recorridos = 0
     solucion= None
     return (num_estados_recorridos, solucion)


######
# FUNCIONES ESPECIFICAS A 8-PUZZLE 
######





# NO CAMBIAR FIRMA DE ESTE METODO (el calificador automatico lo va a usar)
def manhattan(camino, meta) :
    
    # TU CODIGO AQUI - Devuelve la suma de distancias manhattan
    # entre todos los elementos del ultimo estado del camnino  y la meta

    return 0


# NO CAMBIAR FIRMA DE ESTE METODO (el calificador automatico lo va a usar)
def euclidiana(camino, meta) :
    
    # TU CODIGO AQUI - Devuelve la suma de distancias Euclidiana
    # entre todos los elementos del ultimo estado del camnino  y la meta

    return 0
 
# NO CAMBIAR FIRMA DE ESTE METODO (el calificador automatico lo va a usar)
def bad_tiles(camino,meta):
    
    # TU CODIGO AQUI - Devuelve el numero de fichas mal ubicadas en el 
    # ultimo estado

    return 0

# Utilitario que revisa si tu estado es resolvible (en este caso supone que la meta
# es la forma [[1,2,3],[4,5,6],[7,8,0]] pero obviamente esto no siempre es el caso.
#
# Aun asi sirve para generar ejemplos utiles para testeo
#
# Funete: http://math.stackexchange.com/questions/293527/how-to-check-if-a-8-puzzle-is-solvable         
def solvable(estado) :
    invs = 0
    for a in range(len(estado)**2) :
        for b in range(a+1, len(estado)**2) :
             if estado[a/len(estado)][a%len(estado)] == estado[b/len(estado)][b%len(estado)] :
                 invs +=1
    return invs%2 == 0


######
# FUNCIONES ESPECIFICAS A ARAD-BUCAREST
######


# NO CAMBIAR FIRMA DE ESTE METODO (el calificador automatico lo va a usar)
def dist_ciudades(camino,meta):
    # TU CODIGO AQUI
    # Usa funciones especiales para retornar la distancia
    return 0

# Distancia Euclidiana entre la ciudad ingresada y Bucarest
def dist_a_bucarest(ciudad) :
    ROMANIA_EUC = {'arad': 366, 'bucarest': 0, 'craiova': 160, 'dobreta': 242, 'eforie': 161, 
          'fagaras': 176, 'guirgiu': 77, 'hirsova':151, 'iasi': 226, 'lugoj': 244, 'mehadia': 241,
          'neamt': 234, 'oradea':380, 'pitesti':100, 'rimnicu vilcea': 193, 'sibiu':253, 'timisoara':329,
          'urziceni': 80, 'vaslui': 199, 'zerind':374}
    return ROMANIA_EUC[ciudad]

# Esto es basicamente una lista de adyacencia (un grafo) con todas las distancias entre ciudades
# (suponiendo que vas en tren o auto las distancias directas entre ciudades podrian ser mas cortas)
def adyacentes_romania(ciudad) :
    ROMANIA_ADY = { 'arad': (('zerind',75),('timisoara',118),('sibiu', 99)),
                    'timisoara': (('arad',118),('lugoj',111)),
                    'lugoj':(('timisoara',111),('mehadia',70)),
                    'mehadia':(('lugoj',70),('dobreta',75)),
                    'dobreta':(('mehadia',75),('craiova',120)),
                    'craiova':(('dobreta',120),('rimnicu vilcea', 146),('pitesti', 138)),
                    'pitesti':(('craiova',138),('rimnicu vilcea', 97),('bucarest',101)),
                    'rimnicu vilcea':(('craiova',146),('pitesti',97),('sibiu',80)),
                    'sibiu':(('arad',140),('oradea',151),('fagaras',99),('rimnicu vilcea', 80)),
                    'zerind':(('arad',75),('oradea',71)),
                    'fagaras':(('sibiu',99),('bucarest',211)),
                    'bucarest':(('giurgui',90),('pitesti',101),('fagaras',211),('urziceni',85)),
                    'urziceni':(('bucarest',85),('hirsova',98),('vaslui',142)),
                    'hirsova':(('urziceni',98),('eforie',86)),
                    'vaslui':(('urziceni',142),('iasi',92)),
                    'iasi':(('vaslui',92),('neamt',87)),
                    'oradea':(('zerind',71),('sibiu',151)) }
    return ROMANIA_ADY[ciudad] 


##################
# PROBLEMA TRIVIAL
#
# En este problema tu estado inicial es [1]
# y debes llegar a [5]
# Este ejemplo es bueno para depurar

# Estado inicial y objetivo
"""
inicio = [1]
meta = [5]

# Imprime el último elemento de la lista `inicio` correctamente
print(inicio[-1], inicio[-1])

def suc(camino):
    # Genera un nuevo sucesor agregando 1 al último elemento del camino actual
    v = camino[:]
    v.append(camino[-1] + 1)  # Corregido para agregar 1 al último elemento
    return v  # Retorna el nuevo camino

# Llamamos a la función `suc` con el estado inicial y lo imprimimos
nuevo_camino = suc(inicio)
print(nuevo_camino)
"""


#begin = current_time()
#solucion = uc_bfs(inicio, meta, suc, 6)
#print(solucion, current_time()-begin)



#######################################
# Tests
#######################################

##meta = [[1,2,3],[4,5,6],[7,8,0]]
#inicio = [[1,2,3],[4,0,6],[7,5,8]]
#inicio = [[0,1,2],[3,4,5],[6,7,8]]
##inicio = [[8,0,6],[5,4,7],[2,3,1]]


#inicio = [[2,8.3],[1,6,4],[7,0,5]]

#inicio = [[0,1,3],[4,2,5],[7,8,6]]
#meta = [[1,2,3],[8,0,4],[7,6,5]]

##print(manhattan([inicio], meta))


#print(solvable(inicio))

inicio = [[1,2,3],[4,5,6],[7,8,0]]
resultados = sucesores(inicio)
print(resultados)
"""
print('UC-BFS 8-PUZZlLE')
begin = current_time()
solucion = uc_bfs(inicio, meta, sucesores)
print(solucion, current_time()-begin)

print('A* Manhattan 8-Puzzle')
begin = current_time()
solucion = a_estrella(inicio,meta, manhattan, sucesores)
print(solucion, current_time()-begin)

print('A* Bad Tiles 8-Puzzle')
begin = current_time()
solucion = a_estrella(inicio,meta, bad_tiles, sucesores)
print(solucion, current_time()-begin)

print('UC-BFS ciudades')
begin = current_time()
#solucion = uc_bfs(inicio_ciudades, meta_ciudades, suc_ciudades, costo_camino)
#print(solucion, current_time()-begin))

print('A* Dist Eculidiana Ciudades')
begin = current_time()
#solucion = a_estrella(inicio_ciudades, meta_ciudades, tu_heuristica, suc_ciudades, costo_camino)
#print(solucion, current_time()-begin))
"""

