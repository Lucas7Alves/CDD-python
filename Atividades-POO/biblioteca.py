class Pessoa:
    def __init__(self, nome,peso,idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.stsComer = False
        self.stsAndar = False
        self.stsDormir = False

    def andar(self):
        if self.stsAndar == True:
            print(f"{self.nome} já esta andando, não pode andar novamente")
        elif self.stsComer == True:
            print(f"{self.nome} não pode andar pois está comendo")
        elif self.stsDormir == True:
            print(f"{self.nome} não pode andar pois está dormindo")
        else:
            self.stsAndar = True        
            print(f"{self.nome} está andando")
            

    def comer(self):
        if self.stsComer == True:
            print(f"{self.nome} já esta comendo, não pode comer novamente")
        elif self.stsAndar == True:
            print(f"{self.nome} não pode comer pois está andando")
        elif self.stsDormir == True:
            print(f"{self.nome} não pode comer pois está dormindo")
        else:
            self.stsComer = True        
            print(f"{self.nome} está comendo")
            
            

    def dormir(self):
        if self.stsDormir == True:
            print(f"{self.nome} já esta dormindo, não pode dormir novamente")
        elif self.stsAndar == True:
            print(f"{self.nome} não pode dormir pois está andando")
        elif self.stsComer == True:
            print(f"{self.nome} não pode dormir pois está comendo")
        else:
            self.stsDormir = True        
            print(f"{self.nome} está dormindo")    



    def pararAndar(self):
        if self.stsAndar == True:
            self.stsAndar = False
            print(f"{self.nome} parou de andar")
        else:
            print(f"{self.nome} não está andando")
    
    def pararComer(self):
        if self.stsComer == True:
            self.stsComer = False
            print(f"{self.nome} parou de comer")
        else:
            print(f"{self.nome} não está comendo")

    def pararDormindo(self):
        if self.stsDormir == True:
            self.stsDormir = False
            print(f"{self.nome} parou de dormir")
        else:
            print(f"{self.nome} não está dormir")