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
from queue import PriorityQueue

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

    # Obtiene el último estado del camino original
    c=contar_corchetes(str(camino_original))
    t=contar_sublistas(c)
   
    if t == 1:
        ult_estado = camino_original
    else:
        for i, sublista in enumerate(camino_original):
            ult_estado = camino_original[-1]

    print("Ultimo estado fn sucesores: ", ult_estado)
    # Obtiene la posición del espacio en blanco (0)
    fila_vacia, col_vacia = None, None
    for fila in range(len(ult_estado)):
        if 0 in ult_estado[fila]:
            fila_vacia, col_vacia = fila, ult_estado[fila].index(0)
            break
    print("fila_vacia: ", fila_vacia)
    print("col_vacia: ", col_vacia)
    # Genera los movimientos posibles (arriba, abajo, izquierda, derecha)
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Genera los estados sucesores
    sucesores = []
    for fila, col in movimientos:
        nueva_fila_vacia, nueva_col_vacia = fila_vacia + fila, col_vacia + col
        if 0 <= nueva_fila_vacia < len(ult_estado) and 0 <= nueva_col_vacia < len(ult_estado[0]):
            nuevo_estado = [fila.copy() for fila in ult_estado]  # Clona el estado actual
            nuevo_estado[fila_vacia][col_vacia], nuevo_estado[nueva_fila_vacia][nueva_col_vacia] = nuevo_estado[nueva_fila_vacia][nueva_col_vacia], nuevo_estado[fila_vacia][col_vacia]
            print("Nuevo estado  fn sucesores: ", nuevo_estado)
            sucesores.append(nuevo_estado)
    
    # Devuelve una lista de caminos a los sucesores
    sucesores.append(ult_estado)
    #for suc in sucesores:
       #print("Contenido de sucesores: ", suc)

    sucesores.reverse()
    resultado = []
    # Itera sobre la lista original para generar las sublistas
    for i in range(len(sucesores) - 1):
        sublista = [sucesores[i], sucesores[i + 1]]
        resultado.append(sublista)
    print("Return fn sucesores: ", resultado)
    return resultado

def contar_corchetes(lista):
    count = 0
    for elemento in lista:
        if isinstance(elemento, list):
            count += contar_corchetes(elemento)
    return count + lista.count('[')

def contar_sublistas(num):
    count = 0
    if num == 4:
        return 1
    elif num == 9:
        return 2
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

    # Inicializa un conjunto para mantener un registro de los estados visitados
    estados_visitados = set()

    # Inicializa una cola de prioridad para realizar la búsqueda de costo uniforme
    cola_prioridad = PriorityQueue()
    # Agrega el estado inicial a la cola de prioridad con un costo inicial de 0
    cola_prioridad.put((0, [inicio]))
    nuevo_camino = []
    # Inicializa el contador de estados recorridos
    num_estados_recorridos = 0
     # Inicializa una lista para mantener todos los estados recorridos
    estados_recorridos = []

    while not cola_prioridad.empty():
        costo_actual, camino_actual = cola_prioridad.get()
        print("camino actual== ", camino_actual)
        estado_actual = camino_actual[-1]
        print("ESTADO ACTUAL== ", estado_actual)
        if estado_actual == meta:
            # Devuelve el número de estados recorridos y el camino
            # Para ver estados recorridos devolver estados_recorridos
            return num_estados_recorridos, camino_actual

        estado_actual_tupla = tuple(map(tuple, estado_actual))
        estados_visitados.add(estado_actual_tupla)

        estados_recorridos.append(estado_actual)

        for sucesor in sucesores_fn(estado_actual):
            for i in range(len(sucesor)):
                print("sucesor for===",i,"          ", sucesor[i])
                sucesor_tupla = tuple(map(tuple, map(tuple, sucesor[i])))
                if sucesor_tupla not in estados_visitados:
                    print("dentro del if")
                    nuevo_costo = costo_actual + 1
                    nuevo_camino = camino_actual + [sucesor[i]]
                    cola_prioridad.put((nuevo_costo, nuevo_camino))

        num_estados_recorridos += 1

        if num_estados_recorridos >= max_prof:
            break

    return num_estados_recorridos,estados_recorridos


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
     # Inicializa un conjunto para mantener un registro de los estados visitados
    estados_visitados = set()

    # Inicializa una cola de prioridad para realizar la búsqueda de A*
    cola_prioridad = []
    # Agrega el estado inicial a la cola de prioridad con un costo inicial de 0 y una lista vacía de acciones
    heapq.heappush(cola_prioridad, (0, inicio, []))

    # Inicializa el contador de estados recorridos
    num_estados_recorridos = 0

    while cola_prioridad:
        # Obtiene el nodo actual desde la cola de prioridad
        costo_actual, estado_actual, acciones_actual = heapq.heappop(cola_prioridad)

        print ("==========ESTADO ACTUAL               : ", estado_actual)
        # Verifica si el estado actual es el estado objetivo
        if estado_actual == meta:
            print ("!SOLUCION")
            return num_estados_recorridos, inicio + acciones_actual  # Solución encontrada

        # Marca el estado actual como visitado
        estado_actual_tupla = tuple(map(tuple, estado_actual))  # Convertir la lista en una tupla inmutable
        estados_visitados.add(estado_actual_tupla)


        # Genera los sucesores y los agrega a la cola de prioridad si no se han visitado
        for sucesor, accion in sucesores_fn(estado_actual):
            print ("\n                SUCESOR: ", accion)
           
            if tuple(map(tuple, accion)) not in estados_visitados:
                print ("en if")
                # Calcula el costo acumulado hasta este sucesor
                nuevo_costo = costo_actual + 1
                # Calcula el valor heurístico estimado desde este sucesor hasta el objetivo
                heuristica = heuristica_fn(accion,meta)
                print ("Heuristica:", heuristica)
                # Calcula la función de costo total (f = g + h)
                costo_total = nuevo_costo + heuristica
                print ("costo:total:", costo_total, "     nuevo_costo: ", nuevo_costo)
                # Agrega el sucesor a la cola de prioridad con su costo total y acciones acumuladas
                heapq.heappush(cola_prioridad, (costo_total, accion, acciones_actual + [accion]))

        # Incrementa el contador de estados recorridos
        num_estados_recorridos += 1

        # Verifica si se alcanzó la profundidad máxima
        if num_estados_recorridos >= max_prof:
            break  # Evitar bucle infinito en caso de no encontrar una solución

    # Si llegamos aquí, no se encontró una solución
    return num_estados_recorridos, None


######
# FUNCIONES ESPECIFICAS A 8-PUZZLE 
######





# NO CAMBIAR FIRMA DE ESTE METODO (el calificador automatico lo va a usar)
def manhattan(camino, meta) :
    
    # TU CODIGO AQUI - Devuelve la suma de distancias manhattan
    # entre todos los elementos del ultimo estado del camnino  y la meta

    # Obtiene el último estado del camino
    estado_actual = camino
   
    # Inicializa la suma de distancias Manhattan
    suma_distancias = 0

    # Recorre las filas y columnas de los estados actual y meta
    for i in range(len(estado_actual)):
        for j in range(len(estado_actual[i])):
            valor = estado_actual[i][j]
                # Encuentra la posición del valor en el estado objetivo (meta)
            x_meta, y_meta = None, None
            for k in range(len(meta)):
                if valor in meta[k]:
                    x_meta, y_meta = k, meta[k].index(valor)
                    break
                # Calcula la distancia Manhattan y la agrega a la suma
            distancia_manhattan = abs(i - x_meta) + abs(j - y_meta)
            suma_distancias += distancia_manhattan

    return suma_distancias



# NO CAMBIAR FIRMA DE ESTE METODO (el calificador automatico lo va a usar)
def euclidiana(camino, meta) :
    
    # TU CODIGO AQUI - Devuelve la suma de distancias Euclidiana
    # entre todos los elementos del ultimo estado del camnino  y la meta

    return 0
 
# NO CAMBIAR FIRMA DE ESTE METODO (el calificador automatico lo va a usar)
def bad_tiles(camino,meta):
    
    # TU CODIGO AQUI - Devuelve el numero de fichas mal ubicadas en el 
    # ultimo estado
    # Obtiene el último estado del camino
    ultimo_estado = camino
    
    # Inicializa el contador de fichas mal ubicadas
    fichas_mal_ubicadas = 0
    
    # Compara cada ficha del último estado con la ficha correspondiente en el estado objetivo
    for i in range(len(ultimo_estado)):
        for j in range(len(ultimo_estado[i])):
            if ultimo_estado[i][j] != meta[i][j]:
                fichas_mal_ubicadas += 1
    
    return fichas_mal_ubicadas
    

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
    ROMANIA_EUC = {'a': 366, 'bucarest': 0, 'craiova': 160, 'dobreta': 242, 'eforie': 161, 
          'fagaras': 176, 'guirgiu': 77, 'hirsova':151, 'iasi': 226, 'lugoj': 244, 'mehadia': 241,
          'neamt': 234, 'oradea':380, 'pitesti':100, 'rimnicu vilcea': 193, 'sibiu':253, 'timisoara':329,
          'u': 80, 'vaslui': 199, 'zerind':374}
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
    return ROMANIA_ADY.get(ciudad, ())

def adyacentes_ciudades(ciudad) :
    ROMANIA_ADY = { 'arad': (('zerind',"timisoara"),('timisoara',"sibiu"),('sibiu',"sibiu")),
                    'timisoara': (('arad'),('lugoj')),
                    'lugoj':(('timisoara'),('mehadia')),
                    'mehadia':(('lugoj'),('dobreta')),
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
    return ROMANIA_ADY.get(ciudad, ())

# Función para obtener sucesores válidos desde una ciudad
def sucesores_ciudades(ciudad):
    return adyacentes_ciudades(ciudad)

# Función de heurística usando distancia euclidiana
def heuristica_fn(camino,meta):
    ciudad_actual = camino[-1]
    return dist_a_bucarest(ciudad_actual)

# Función de costo acumulado
def costo_camino_fn(camino):
    costo = 0
    for i in range(1, len(camino)):
        ciudad_actual, ciudad_anterior = camino[i], camino[i - 1]
        for adyacente, distancia in adyacentes_romania(ciudad_anterior):
            if adyacente == ciudad_actual:
                costo += distancia
                break
    return costo
##################
# PROBLEMA TRIVIAL
#
# En este problema tu estado inicial es [1]
# y debes llegar a [5]
# Este ejemplo es bueno para depurar

# Estado inicial y objetivo



#begin = current_time()
#solucion = uc_bfs(inicio, meta, suc, 6)
#print(solucion, current_time()-begin)



#######################################
# Tests
#######################################

meta = [[1,2,3],[4,5,6],[7,8,0]]
inicio = [[1,2,3],[4,0,6],[7,5,8]]
#-inicio = [[0,1,2],[3,4,5],[6,7,8]]
#-inicio = [[8,0,6],[5,4,7],[2,3,1]]


#+inicio = [[2,8,3],[1,6,4],[7,0,5]]

#+inicio = [[0,1,3],[4,2,5],[7,8,6]]
#meta = [[1,2,3],[8,0,4],[7,6,5]]

#print(manhattan([inicio], meta))


#print(solvable(inicio))

""" mi test
inicio = [[1,2,3],[4,5,6],[7,8,0]]
resultados = sucesores(inicio)
print(resultados)
"""

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
"""
inicio_ciudades = 'arad'
meta_ciudades = 'bucharest'

"""
print('UC-BFS ciudades')
begin = current_time()
#solucion = uc_bfs(inicio_ciudades, meta_ciudades, suc_ciudades, costo_camino)
#print(solucion, current_time()-begin))
"""
print('A* Dist Eculidiana Ciudades')
begin = current_time()
solucion = a_estrella(inicio_ciudades, meta_ciudades, heuristica_fn,sucesores_ciudades, costo_camino_fn)
print(solucion, current_time()-begin)

"""
print('A* Dist Eculidiana Ciudades')
begin = current_time()
solucion = a_estrella(inicio_ciudades, meta_ciudades, tu_heuristica, suc_ciudades, costo_camino)
print(solucion, current_time()-begin)
"""
