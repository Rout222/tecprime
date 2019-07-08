# coding=utf-8

from flask import Flask, jsonify, request, abort
from flask_cors import CORS

from tinydb import TinyDB, Query
db = TinyDB('./db.json')

from entities.user import User, UserSchema

import urllib.request, json  # pra cuidar da requisição da outra API

from math import ceil

#from entities.user import User
# Criando aplicação
app = Flask(__name__)
CORS(app)
API_URL = 'https://reqres.in/api/users?page={}&per_page={}'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}


@app.route('/users', methods=['GET']) # pegar dados
def getUsers():


    #pra manusear os argumentos do flask
    try:
        if int(request.args['per_page']):
            per_page = int(request.args['per_page'])
    except:
        per_page = 3

    try:
        if int(request.args['page']):
            page = int(request.args['page'])
    except:
        page = 1

    #pegando os dados da API web
    req = urllib.request.Request(API_URL.format(page, per_page), headers = headers)
    with urllib.request.urlopen(req) as response:
       data = json.loads(response.read().decode())
       api_users = data['data']
       api_total = int(data['total'])
    
    #pegando os dados do TINYDB
    tinydb_users = db.table('users').all()

    # transofrmando em json
    schema = UserSchema(many=True)
    dados = schema.dump(api_users)

    #montando a resposta final
    total = api_total + len(db.table('users'))

    data = api_users
    #juntando as duas API caso a URL não for suficiente
    if len(api_users) != per_page:
        if(len(api_users) != 0):
            datamin = 0
        else:
            datamin = ceil(((page * per_page) - api_total)/per_page)-1
        datamax = datamin + per_page
        dadostotal = api_users + tinydb_users
        data = dadostotal[datamin:datamax]
    res = {"page" : page, 'per_page' : per_page, "total" : total, 'total_pages' : ceil(total/per_page), "data": data}
    return jsonify(res)

@app.route('/users/<int:id>', methods=['GET']) # pegar um usuário
def getUser(id):

    per_page = 1
    page = id

    #pegando os dados da API web
    req = urllib.request.Request(API_URL.format(page, per_page), headers = headers)
    with urllib.request.urlopen(req) as response:
       data = json.loads(response.read().decode())
       api_users = data['data']
       api_total = int(data['total'])
    
    #pegando os dados do TINYDB
    tinydb_users = db.table('users').all()

    # transofrmando em json
    schema = UserSchema(many=True)
    dados = schema.dump(api_users)

    #montando a resposta final
    total = api_total + len(db.table('users'))

    data = api_users
    #juntando as duas API caso a URL não for suficiente
    if len(api_users) != per_page:
        if(len(api_users) != 0):
            datamin = 0
        else:
            datamin = ceil(((page * per_page) - api_total)/per_page)-1
        datamax = datamin + per_page
        dadostotal = api_users + tinydb_users
        data = dadostotal[datamin:datamax]
    res = data
    if(len(data) == 0):
        abort(404)
    else:
        return jsonify(res)

@app.route('/users', methods=['POST'])
def addUser():
    # montar o usuário
    posted_user = UserSchema(only=('email', 'first_name', 'last_name', 'avatar')).load(request.get_json())

    user = User(**posted_user.data)

    # salvar
    db.table('users').insert(user.save())

    # retornar
    novo_user = UserSchema().dump(user).data

    return jsonify(novo_user), 201



@app.route('/users/<int:id>', methods=['PUT'])
def updateUser(id):
    # montar o usuário
    posted_user = UserSchema(only=('email', 'first_name', 'last_name', 'avatar')).load(request.get_json())

    user = User(**posted_user.data)

    #bom, temos dois casos aqui, se for pra editar um usuário da API, então salva ele editado no banco de dados, caso contrário edite ele.
    #pegando os dados da API web
    req = urllib.request.Request(API_URL.format(id, 1), headers = headers)
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        api_user = data['data']

        if(len(api_user) > 0): #se existe é na APIWEB
            # caso a API fosse integrada
            #deleteFromAPI(id)

            # salvar no banco de dados local
            db.table('users').insert(user.save())

        else: #caso contrário edita no banco
            api_total = int(data['total'])
            idtinyDB = id-api_total
            db.table('users').update(user.save(), doc_ids=[idtinyDB])

    return ('', 200)