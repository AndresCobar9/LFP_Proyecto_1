AfdOptimizados = []

def minimizar_AFD(afd, nombre):
    particiones = [set(afd.estados_aceptacion), set(afd.estados) - set(afd.estados_aceptacion)]

    while True:
        nuevas_particiones = []

        for particion in particiones:
            nuevos_grupos = particionar(afd, particion, particiones)
            nuevas_particiones.extend(nuevos_grupos)

        if len(nuevas_particiones) == len(particiones):
            break

        particiones = nuevas_particiones
    print('por aca 1')
    estados_minimizados = []
    transiciones_minimizadas = {}

    for i, particion in enumerate(particiones):
        estado_minimizado = ','.join(sorted(list(particion)))
        estados_minimizados.append(estado_minimizado)

        for simbolo in afd.alfabeto:
            siguiente_estado = obtener_siguiente_estado(afd, particion, simbolo)
            siguiente_estado_minimizado = ','.join(sorted(list(siguiente_estado)))

            transiciones_minimizadas.setdefault(estado_minimizado, {})[simbolo] = siguiente_estado_minimizado
    print('por aca 3')
    afd_minimizado = AFDMinimizado(
        nombre=nombre,
        alfabeto=afd.alfabeto,
        estados=estados_minimizados,
        estado_inicial=','.join(sorted(list(particiones[0]))),
        estados_aceptacion=obtener_estados_aceptacion_minimizados(afd, particiones),
        transiciones=transiciones_minimizadas
    )
    AfdOptimizados.append(afd_minimizado)
    return afd_minimizado

def listaAFD():
    return AfdOptimizados

def particionar(afd, particion, particiones):
    nuevos_grupos = []

    for simbolo in afd.alfabeto:
        grupo_transiciones = {}

        for estado in particion:
            siguiente_estado = afd.transiciones[estado].get(simbolo)
            
            if siguiente_estado is None:
                continue

            for i, particion_existente in enumerate(particiones):
                if siguiente_estado in particion_existente:
                    grupo_transiciones.setdefault(i, set()).add(estado)
                    break
            else:
                grupo_transiciones.setdefault(len(particiones), set()).add(estado)

        nuevos_grupos.extend(grupo_transiciones.values())

    return nuevos_grupos


def obtener_siguiente_estado(afd, particion, simbolo):
    siguiente_estado = set()

    for estado in particion:
        siguiente_estado.add(afd.transiciones[estado].get(simbolo))

    return siguiente_estado


def obtener_estados_aceptacion_minimizados(afd, particiones):
    estados_aceptacion_minimizados = set()

    for i, particion in enumerate(particiones):
        for estado in particion:
            if estado in afd.estados_aceptacion:
                estados_aceptacion_minimizados.add(i)

    return list(estados_aceptacion_minimizados)


class AFDMinimizado:
    def __init__(self, nombre, alfabeto, estados, estado_inicial, estados_aceptacion, transiciones):
        self.nombre = nombre
        self.alfabeto = alfabeto
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = transiciones
