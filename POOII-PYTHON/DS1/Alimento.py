class Alimentos:
    def __init__(self, nome, quantidadeG, calorias, macronutientes=None):
        self.nome =  nome
        self.quantidadeG = quantidadeG
        self.calorias = calorias
        self.macronutrientes = macronutientes if macronutientes else {"proteína": 0, "carboidratos": 0, "gorduras": 0}