class Dados:
    def __init__(self, nome='', cargo_desejado='', formacao='', experiencias='', skills='', foto='', telefone=''):
        self.nome = nome
        self.cargo_desejado = cargo_desejado
        self.formacao = formacao
        self.experiencias = list(experiencias)
        self.skills = list(skills)
        self.foto = foto
        self.telefone = list(telefone)

    def entrada_dados(self):
        self.nome = input('Nome: ')
        self.cargo_desejado = input('Cargo desejado: ')
        self.formacao = input('Formação: ')
        self.experiencias = input('Experiência(s): ').split(',')
        self.skills = input('Habilidade(s): ').split(',') 
        self.telefone = input("Telefone: ")
        self.foto = input("Foto: ")