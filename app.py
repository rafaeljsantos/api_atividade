from flask import Flask
from flask_restful import Resource, Api, request
from models import Pessoas, Atividades, Usuarios
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()

app = Flask(__name__)
api = Api(app)

USUARIOS = {
    'rafael': '123',
    'santos': '456'
}


@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class Pessoa(Resource):
    @auth.login_required
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': "Pessoa não encontrada."
            }
        return response

    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        try:
            pessoa.save()
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                "status": "error",
                "mensagem": "Pessoa Não encontrada"
            }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = "Pessoa {} excluida com sucesso.".format(pessoa.nome)
        response = {
            'status': 'sucesso',
            'mensagem': mensagem
        }
        try:
            pessoa.delete()
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': "Pessoa não encontrada."
            }
        return response


class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{
            'id': i.id,
            'nome': i.nome,
            'pessoa': i.pessoa
        } for i in atividades]

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['nome']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)
