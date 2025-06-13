from services.repositorio import Database
import os
from dotenv import load_dotenv

def buscar_todas_as_mensagens() -> dict | None:
    db = Database()
    usuarios = db.buscar_todos_usuarios_em_dict()
    db.encerrar_sessao()
    return usuarios

def buscar_dados_config() -> dict | None:
    db = Database()

    load_dotenv()
    llm_selecionada = db.buscar_llm_disponivel()
    lista_ia = db.buscar_todas_ia()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')

    lista_llm = []

    for ia in lista_ia:
        if ia.get('nome') == "GroqAI":
            ia['api_key'] = GROQ_API_KEY
            lista_llm.append(ia)
        if ia.get('nome') == "ChatGPT":
            ia['api_key'] = OPENAI_API_KEY
            lista_llm.append(ia)
        if ia.get('nome') == "Gemini":
            ia['api_key'] = GOOGLE_API_KEY
            lista_llm.append(ia)

    for ia in lista_llm:
        if ia.get('nome') == llm_selecionada:
            ia['ia_selecionada'] = True

    dados = {
        "llm": lista_llm,
        "powerBI": "www.powerBI.com"
    }

    db.encerrar_sessao()
    return dados

def salvar_novas_config(dados: dict):
    db = Database()
    llm_nova = dados.get('ia')
    db.atualizar_llm(llm_nova)
    db.encerrar_sessao()

