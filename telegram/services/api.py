from flask import Flask, jsonify, request
from flask_cors import CORS

import os
from dotenv import load_dotenv

# from responder_mensagens import obter_id_telegram
# from telegram import enviar_mensagem

load_dotenv()
HOST = os.getenv('API_HOST')
PORT = int(os.getenv('API_PORT'))

def montar_API():
    # motando API
    app = Flask(__name__)
    CORS(app)

    # responder mensagem do usuário:
    @app.route('/telebot/enviar', methods=['POST'])
    def enviar_resposta():
        dados = request.get_json()

        # # obter ID Telegram:
        # id_telegram = obter_id_telegram(dados.get('usuario'))

        # # enviar mensagem ao usuário
        # enviar_mensagem(id_telegram, dados.get('resposta'))

        # return jsonify({'dados': dados})  

    app.run(port=PORT,host=HOST,debug=False)

if __name__ == "__main__":
    montar_API()