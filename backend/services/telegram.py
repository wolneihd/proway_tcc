import os
import telebot
from dotenv import load_dotenv
from entities.Mensagem import Mensagem
import io
from services.audio_handler import convert_audio_memoria, transcribe_audio_memoria
from services.salvar_minio import salvar_imagem_bucket, salvar_audio_bucket

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
    response = mensagem.retorno_usuario()
    bot.send_message(message.chat.id, response)

## Handler para mensagens em audio
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    try:
        # Baixa o arquivo de áudio
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # atualizado para salvar audio em memória para economizar armazenamento.
        ogg_file = io.BytesIO(downloaded_file)
        wav_file = convert_audio_memoria(ogg_file)
        transcription = transcribe_audio_memoria(wav_file)

        # salvando arquivo no MinIO:
        nome_arquivo = salvar_audio_bucket(downloaded_file)

        mensagem = Mensagem(user=message, endereco_arquivo=nome_arquivo, transcricao_audio=transcription)
        response = mensagem.retorno_usuario()

        bot.send_message(message.chat.id, response)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "Erro ao processar a imagem. Favor tentar novamente mais tarde.")   

## Handler para mensagens tipo Imagem
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    try:
        # Obtém o arquivo da imagem
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        nome_arquivo = salvar_imagem_bucket(downloaded_file)

        mensagem = Mensagem(user=message, endereco_arquivo=nome_arquivo, transcricao_audio=None)
        response = mensagem.retorno_usuario()

        bot.send_message(message.chat.id, response)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "Erro ao processar a imagem. Favor tentar novamente mais tarde.")    
    

def iniciar_telebot():
    print(">>> Bot Telegram inicializado...")
    bot.polling(none_stop=True)

if __name__ == "__main__":
    iniciar_telebot()