class nodo():
    def __init__(self, valor):
        self.valor=valor
        self.Izq=None
        self.Der=None
        pass

    def getArbol(self):
        strOut = ""
        strOut += f" NP[{self.valor}] "
        if type(self.Izq) != type(None):
            strOut += f" Iz[{self.valor}]->[{self.Izq}] "
        
        if self.Der is not None:
            strOut += f" Dr[{self.valor}]->[{self.Der}] "

        return strOut

    def __str__(self):
        return f"valor: {self.valor}"



pass