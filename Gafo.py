import queue
from graphviz import Source

def graficar(raiz):
    acumulador = ["digraph G\n{\nnode[shape = record, height= .1];\n", "", 0, 0]
    if raiz != None:
        cola = queue.Queue()
        cola.put(raiz)
        while not(cola.empty()):
            tmpPagina = cola.get()
            imprimir(tmpPagina, acumulador)
            i = 0
            while i <= tmpPagina.cuenta:
                if tmpPagina.ramas[i] != None:
                    cola.put(tmpPagina.ramas[i])
                i += 1
            acumulador[2] += 1
        acumulador[0] += "\n" + acumulador[1]

    acumulador[0] += "}\n"
    src = Source(acumulador[0], filename="arbolb5", format="svg")
    src.view()

def imprimir(actual, acumulador):
    acumulador[0] += 'node{}[label="<r0>'.format(str(acumulador[2]))

    if actual.ramas[0] != None:
        acumulador[3] += 1
        acumulador[1] += '"node{}":r0 -> "node{}"\n'.format(str(acumulador[2]) , str(acumulador[3]))

    i = 1
    while i <= actual.cuenta:
        acumulador[0] += '|<c{}> {} |<r{}>'.format(str(i),str(actual.claves[i]),str(i))

        if actual.ramas[i] != None:
            acumulador[3] += 1
            acumulador[1] += '"node{}":r{} -> "node{}"\n'.format(str(acumulador[2]) ,str(i), str(acumulador[3]))
        i += 1
    acumulador[0] += '"];\n'