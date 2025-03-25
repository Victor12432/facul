class Pessoa:
    #Construtor
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    #Usamos @property para definir getters e setters, _ está sendo usado para privar os atributos
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, v):
       self._name = v

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, v):
        self._age = v

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, v):
        self._weight = v

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, v):
        self._height = v