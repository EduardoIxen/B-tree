from Gafo import graficar
from ArbolB import ArbolB

arbol = ArbolB(5)
arbol.insertar(3)
arbol.insertar(2)
arbol.insertar(6)
arbol.insertar(9)
arbol.insertar(22)
arbol.insertar(7)
arbol.insertar(8)
arbol.insertar(14)
arbol.insertar(19)
arbol.insertar(17)

graficar(arbol.raiz)