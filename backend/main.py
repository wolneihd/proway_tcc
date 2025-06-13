from services.telegram import iniciar_telebot
from services.api import montar_API
import threading
from services.repositorio import Database

def montar_aplicacao():
    
    db = Database()
    db.criar_database_se_nao_existir()
    db.criar_tabelas()
    db.migracao_dados()

    # O iniciar_telebot será executado na main thread para evitar o erro
    thread_api = threading.Thread(target=montar_API)
    
    # Inicializa as threads
    thread_api.start()

    # Iniciar o bot na thread principal
    iniciar_telebot()

if __name__ == '__main__':
    montar_aplicacao()
