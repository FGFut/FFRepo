from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
import _mysql_connector
import json

#usar python 3.8

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:2412Lulu.@localhost/cadastro'

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(8))

    def to_json(self):
        return {"id":self.id, "name": self.name, "email":self.email, "senha": self.senha}


db.create_all()

#Selecionar Tudo - GET
@app.route('/usuarios', methods = ["GET"])
def seleciona_usuarios():
    usuarios_objetos = Usuario.query.all()
    usuarios_json = [usuario.to_json() for usuario in usuarios_objetos]
    print(usuarios_json)
    return gera_response(200, "usuarios", usuarios_json, "ok")

#Selecionar individualmente - GET by id
@app.route('/usuarios/<id>', methods = ["GET"])
def seleciona_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    usuario_json = usuario_objeto.to_json()
    return gera_response(200, "usuario", usuario_json)

#Cadastrar - POST

@app.route('/usuario', methods = ["POST"])
def criar_usuario():
    body = request.get_json()

    try:
        usuario = Usuario(name=body["name"], email=body["email"], senha=body["senha"])
        db.session.add(usuario)
        db.session.commit()
        return gera_response(201, "usuario", usuario.to_json(), "Criado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "usuario", {}, "Erro ao cadastrar")

#Atualizar - PUT
@app.route('/usuario/<id>', methods = ["PUT"])
def atualiza_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    body = request.get_json()
    
    try:
        if('name' in body):
            usuario_objeto.name = body['name']
        if('email' in body):
            usuario_objeto.email = body['email']
        if('senha' in body):
            usuario_objeto.senha = body['senha']

        db.session.add(usuario_objeto)
        db.session.commit()
        return gera_response(200, "usuario", usuario_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "usuario", {}, "Erro ao atualizar")

#Deletar - DELETE
@app.route('/usuario/<id>', methods = ["DELETE"])
def deleta_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()

    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        return gera_response(200, "usuario", usuario_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "usuario", {}, "Erro ao deletar")

@app.route('/homepage.html')
def homepage():
    return render_template('homepage.html')

@app.route('/cadastro.html')
def cadastrar():
    return render_template('cadastro.html')

@app.route('/login.html')
def entrar():
    return render_template('login.html')

@app.route('/partidas.html')
def partidas():
    return render_template('partidas.html')



def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo
 
    if(mensagem):
        body["mensagem"] = mensagem

    return Response(json.dumps(body) , status = status, mimetype="application/json")


app.run()

