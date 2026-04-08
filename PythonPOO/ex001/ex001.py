class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade = self.idade +1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade"


g1 = Gafanhoto()
g1.nome = "Afonso"
g1.idade = 10
print(g1.mensagem())