class AFDoptimizado:
    def __init__(self, nombre, alfabeto, estados, estado_inicial, estados_aceptacion, transiciones):
        self.nombre = nombre
        self.alfabeto = alfabeto
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = transiciones

    def __str__(self):
        estados_str = ", ".join(self.estados)
        alfabeto_str = ", ".join(self.alfabeto)
        estados_aceptacion_str = ", ".join(self.estados_aceptacion)
        transiciones_str = str(self.transiciones)

        return f"Nombre: {self.nombre}\nEstados: {estados_str}\nAlfabeto: {alfabeto_str}\nEstado Inicial: {self.estado_inicial}\nEstados de Aceptación: {estados_aceptacion_str}\nTransiciones:\n{transiciones_str}"


def minimizar_AFD(afd, nombre_nuevo):
    nombre = nombre_nuevo
    alfabeto = afd.alfabeto
    estados = afd.estados
    estado_inicial = afd.estado_inicial
    estados_aceptacion = afd.estados_aceptacion

    # Obtener las transiciones en el formato {'estado': {'simbolo': 'estado_siguiente'}}
    transiciones = afd.transiciones

    # Obtener los estados distinguibles utilizando el algoritmo de Moore
    estados_distingibles = obtener_estados_distingibles(transiciones)

    # Crear un nuevo objeto AFDoptimizado con los estados minimizados
    afd_minimizado = AFDoptimizado(nombre, alfabeto, estados_distingibles.keys(), estado_inicial, estados_aceptacion, estados_distingibles)

    return afd_minimizado


def obtener_estados_distingibles(transiciones):
    estados = list(transiciones.keys())
    alfabeto = list(transiciones[estados[0]].keys())

    # Inicializar la lista de pares de estados distingibles
    pares_distingibles = []

    # Paso 1: Dividir los estados en dos conjuntos: estados de aceptación y no aceptación
    estados_aceptacion = []
    estados_no_aceptacion = []
    for estado in estados:
        if estado in estados_aceptacion:
            estados_aceptacion.append(estado)
        else:
            estados_no_aceptacion.append(estado)

    # Paso 2: Agregar los pares (estados de aceptación, estados no aceptación) a la lista de pares distingibles
    for estado_aceptacion in estados_aceptacion:
        for estado_no_aceptacion in estados_no_aceptacion:
            pares_distingibles.append((estado_aceptacion, estado_no_aceptacion))

    # Paso 3: Realizar el proceso de partición hasta que no se encuentren nuevos pares distingibles
    while True:
        nuevos_pares_distingibles = []

        # Iterar sobre los pares distingibles existentes
        for par_distingible in pares_distingibles:
            estado_1, estado_2 = par_distingible

            # Verificar si los estados son distingibles para cada símbolo del alfabeto
            son_distingibles = False
            for simbolo in alfabeto:
                estado_siguiente_1 = transiciones[estado_1][simbolo]
                estado_siguiente_2 = transiciones[estado_2][simbolo]

                # Verificar si los estados siguientes son diferentes
                if estado_siguiente_1 != estado_siguiente_2:
                    # Verificar si el par de estados siguientes no está en la lista de pares distingibles
                    if (estado_siguiente_1, estado_siguiente_2) not in pares_distingibles and (estado_siguiente_2, estado_siguiente_1) not in pares_distingibles:
                        nuevos_pares_distingibles.append((estado_1, estado_2))
                        son_distingibles = True
                        break

            # Si los estados no son distingibles, agregar el par a la lista de nuevos pares distingibles
            if not son_distingibles:
                nuevos_pares_distingibles.append((estado_1, estado_2))

        # Verificar si no se encontraron nuevos pares distingibles
        if len(nuevos_pares_distingibles) == len(pares_distingibles):
            break

        # Actualizar la lista de pares distingibles con los nuevos pares encontrados
        pares_distingibles = nuevos_pares_distingibles

    # Paso 4: Crear los nuevos estados a partir de los pares distingibles
    estados_distingibles = {}
    for par_distingible in pares_distingibles:
        estado_1, estado_2 = par_distingible

        # Verificar si el estado 1 ya existe en los estados distingibles
        if estado_1 in estados_distingibles:
            # Agregar el estado 2 a la lista de estados distingibles del estado 1
            estados_distingibles[estado_1].append(estado_2)
        else:
            # Crear una nueva entrada en los estados distingibles con el estado 1 y el estado 2
            estados_distingibles[estado_1] = [estado_1, estado_2]

    # Retornar los estados distingibles
    return estados_distingibles
