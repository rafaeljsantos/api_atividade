from models import Pessoas, Usuarios


def insere_pessoas():
    pessoa = Pessoas(nome='Rafael', idade=33)
    pessoa.save()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.nome = 'Rafael'
    pessoa.save()


def deleta_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Rafael').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()


def consulta_usuarios():
    usuario = Usuarios.query.all()
    print(usuario)


if __name__ == "__main__":
    insere_usuario('rafael', '1234')
    consulta_usuarios()
