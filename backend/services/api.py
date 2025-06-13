from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
from services.buscar_dados import buscar_todas_as_mensagens

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
    @app.route('/mensagens', methods=['GET'])
    def obter_todas_mensagens():
        dados = buscar_todas_as_mensagens()
        return jsonify(dados)  

    app.run(port=PORT,host=HOST,debug=False)

if __name__ == "__main__":
    montar_API()