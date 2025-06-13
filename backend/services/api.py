from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv
from services.buscar_dados import buscar_todas_as_mensagens, buscar_dados_config, salvar_novas_config
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
    
    # obter todas as LLMS:
    @app.route('/configs', methods=['GET'])
    def obter_todas_opcoes_llm():
        response = buscar_dados_config()
        return jsonify(response)
    
    # salvar salvar configurações novas:
    @app.route('/salvar-config', methods=['POST'])
    def salvar_ia():
        dados = request.get_json()
        response = salvar_novas_config(dados)
        return jsonify(None)  

    # ============================================== TODO  
    
    # obter todas as mensagens:
    @app.route('/filtrar', methods=['POST'])
    def filtrar_mensagens():
        dados = request.get_json()
        return jsonify(None)  

    # gerar sugestão resposta com IA:
    @app.route('/gerar_resposta', methods=['POST'])
    def gerar_resposta():
        dados = request.get_json()
        return jsonify(None)  
    
    # salvar mensagem do totem de feedback:
    @app.route('/totem', methods=['POST'])
    def salvar_mensagem():
        dados = request.get_json()
        return jsonify(None)  

    # obter todas as mensagens:
    @app.route('/totem', methods=['GET'])
    def quantidades_totem():
        dados = request.get_json()
        return jsonify(None)  

    # obter todas os usuarios:
    @app.route('/usuarios', methods=['GET'])
    def obter_todos_usuarios():
        dados = request.get_json()
        return jsonify(None)  
    
    # salvar mensagem do totem de feedback:
    @app.route('/salvar_usuario', methods=['POST'])
    def salvar_usuario():
        dados = request.get_json()
        return jsonify(None)  
    
    # Reenvio de senha por e-mail
    @app.route('/reenvio_senha', methods=['POST'])
    def reenvio_senha():
        dados = request.get_json()
        return jsonify(None)  

    app.run(port=PORT,host=HOST,debug=False)

if __name__ == "__main__":
    montar_API()