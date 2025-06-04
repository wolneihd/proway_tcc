import os
import telebot
from dotenv import load_dotenv
from entities.Mensagem import Mensagem

# Carregar variáveis de ambiente
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

## Resposta ao iniciar o BOT
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Olá, você está no IA-Feedback-Analyser!")

## Handler para mensagens em texto
@bot.message_handler(content_types=['text'])
def handle_text(message):
    mensagem = Mensagem(message)
    mensagem.salvar_dados_banco_dados()
    bot.send_message(message.chat.id, "mensagem recebida, estaremos analisando.")

def iniciar_telebot():
    print(">>> Bot Telegram inicializado...")
    bot.polling(none_stop=True)

if __name__ == "__main__":
    iniciar_telebot()