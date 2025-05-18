from modelo import Dados
from gerador_de_curriculo import Pdf

usuario = Dados()
file = Pdf()

usuario.entrada_dados()
file.titulo()
file.topicos(
    usuario.nome,
    usuario.cargo_desejado,
    usuario.formacao,
    ", ".join(usuario.experiencias),
    ", ".join(usuario.skills),
    usuario.telefone,
)
file.imagem(usuario.foto)
file.save()
     


