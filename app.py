from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {
         'id': '0',
         'nome': 'Ramom',
         'habilidades': ['Python', 'Flask']},
    {
         'id': '1',
         'nome': 'Filho',
         'habilidades': ['Python', 'Django']}
]

#Devolve um Desenvolvedor pelo ID, altera e delete pelo ID.
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}

        except Exception:
            mensagem = 'Erro desconhecido. Procure o ADM da API.'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'Registro escluido'})


#Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods=['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = str(posicao)
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)



if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/soma/<int:valor1>/<int:valor2>')
# def soma(valor1, valor2):
#     return jsonify({'soma': valor1+valor2})


# @app.route('/soma', methods=['POST', 'GET'])
# def soma():
#     if request.method == 'POST':
#         dados = json.loads(request.data)
#         total = sum(dados['valores'])
#     elif request.method == 'GET':
#         total = 10 + 10
#     return jsonify({'soma': total})



