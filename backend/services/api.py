from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
from services.buscar_dados import buscar_todas_as_mensagens
from services.telegram import enviar_mensagem

load_dotenv()
HOST = os.getenv('API_HOST')
PORT = int(os.getenv('API_PORT'))

def montar_API():
    # motando API
    app = Flask(__name__)
    CORS(app)

    # obter todas mensagens:
    @app.route('/mensagens', methods=['GET'])
    def obter_todas_mensagens():
        dados = buscar_todas_as_mensagens()
        return jsonify(dados)  

    # responder mensagem do usuário:
    @app.route('/enviar/resposta', methods=['POST'])
    def enviar_resposta():
        dados = request.get_json()
        id_telegram = dados.get('id_telegram')
        resposta = dados.get('resposta')
        enviar_mensagem(id_telegram, resposta)
        return jsonify({'dados': dados})  

    app.run(port=PORT,host=HOST,debug=False)

if __name__ == "__main__":
    montar_API()