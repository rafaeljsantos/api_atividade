from models import Pessoas


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


if __name__ == "__main__":
    consulta_pessoas()
