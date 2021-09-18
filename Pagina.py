class Pagina:
    def __init__(self, _m):
        self.cuenta = 0
        self.m = _m 
        self.claves = [0 for x in range(_m)]
        self.ramas = [Pagina for x in range(_m)]

        for i in range(_m):
            self.ramas[i] = None
        
    def claves_maximas(self):
        return self.cuenta == self.m - 1
