class Usuario(Pessoa): # type: ignore
    def __int__(self, name, age, weight, height, obv):
        super().__int__(name)
        super().__int__(age)
        super().__int__(weight)
        super().__int__(height)
        self.obv = obv

    @property
    def obv(self):
        return self._obv
    @obv.setter
    def obv(self, v):
       op = "perda de peso, manutenção, ganho de massa"
       if op.count(v) == 1 :
            self._obv = v
        
'''
calculo 
           66+(13,7*peso(kg))+(5*altura(cm))-(6,8*idade) ---> homem
           655+(9,6*peso(kg))+(1,8*altura(cm))-(4,7*idade) ---> mulher
           
           Nível de Atividade	Fator
Sedentário (pouco ou nenhum exercício)	1,2
Leve (exercício leve 1-3 dias/semana)	1,375
Moderado (exercício moderado 3-5 dias/semana)	1,55
Ativo (exercício intenso 6-7 dias/semana)	1,725
Muito Ativo (trabalho físico pesado ou atleta)	1,9
'''