from Pagina import Pagina
import copy

class ArbolB:
    def __init__(self, _orden):
        self.orden = _orden
        self.raiz = Pagina(5)

    def insertar(self, valor):
        array_valores = [False, 0, None, None]
        self.empujar(self.raiz, valor, array_valores)
        if array_valores[0]:
            array_valores[3] = Pagina(self.orden)
            array_valores[3].cuenta = 1
            array_valores[3].claves[1] = array_valores[1]
            array_valores[3].ramas[0] = self.raiz
            array_valores[3].ramas[1] = array_valores[2]
            self.raiz = array_valores[3]

    def empujar(self, pagina_actual, valor, flag_pagina):
        camino = [0]
        if pagina_actual == None:
            flag_pagina[0] = True
            flag_pagina[1] = valor
            flag_pagina[2] = None
        else:
            esta = self.buscarPagina(pagina_actual, valor, camino)
            if esta:
                flag_pagina[0] = False
                return
            self.empujar(pagina_actual.ramas[camino[0]], valor, flag_pagina)
            if flag_pagina[0]:
                if pagina_actual.claves_maximas():
                    self.dividirNodo(pagina_actual,flag_pagina[1],copy.deepcopy(flag_pagina[2]),camino,flag_pagina)
                else:
                    flag_pagina[0] = False
                    self.meterHoja(pagina_actual,flag_pagina[1],flag_pagina[2],camino[0])

    def buscarPagina(self,pagina_actual, valor, camino):
        encontrado = False
        if valor < pagina_actual.claves[1] :
            camino[0] = 0
            encontrado = False
        else:
            camino[0] = pagina_actual.cuenta
            while (valor < pagina_actual.claves[camino[0]]) and (camino[0] > 1):
                camino[0] = camino[0] - 1
            encontrado = valor == pagina_actual.claves[camino[0]]
        return encontrado

    def meterHoja(self , actual, valor, rd, k):
        i = actual.cuenta
        while i >= k + 1:
            actual.claves[i + 1] = actual.claves[i]
            actual.ramas[i + 1] = actual.ramas[i]
            i = i-1
        actual.claves[k + 1] = valor
        actual.ramas[k + 1] = rd
        actual.cuenta = actual.cuenta + 1

    def dividirNodo(self, pagina_actual, valor, rd, camino, flag_pagina):
        posMdna = self.orden / 2 if (camino[0] <= self.orden / 2) else self.orden / 2 + 1
        posMdna = int(posMdna)
        flag_pagina[2] = Pagina(5)
        i = posMdna + 1
        while i < self.orden:
            flag_pagina[2].claves[i - posMdna] = pagina_actual.claves[i]
            flag_pagina[2].ramas[i - 1] = pagina_actual.ramas[i]
            i = i + 1
        flag_pagina[2].cuenta = (self.orden -1) - posMdna
        pagina_actual.cuenta = posMdna
        if camino[0] <= self.orden / 2:
            self.meterHoja(pagina_actual,valor, rd, camino[0])
        else:
            self.meterHoja(flag_pagina[2], valor, rd, camino[0] - posMdna)
        flag_pagina[1] = pagina_actual.claves[pagina_actual.cuenta]
        flag_pagina[2].ramas[0] = pagina_actual.ramas[pagina_actual.cuenta]
        pagina_actual.cuenta = pagina_actual.cuenta -1

