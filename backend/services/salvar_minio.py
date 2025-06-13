import io
import random
import string
from minio import Minio
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
MINIO_API_HOST = os.environ.get('MINIO_API_HOST')
BUCKET = os.environ.get('BUCKET')

MINIO_CLIENT = Minio("minio:9000", access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)

def salvar_imagem_bucket(downloaded_file):

    caracteres = string.ascii_letters + string.digits
    nome_arquivo = ''.join(random.choice(caracteres) for _ in range(15))

    # Enviar a imagem diretamente para o Minio
    try:

        from minio import Minio
        load_dotenv()
        
        MINIO_CLIENT = Minio("host.docker.internal:9000", access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)

        # Envia o arquivo para o Minio diretamente da memória sem salvar localmente
        file_stream = io.BytesIO(downloaded_file)

        MINIO_CLIENT.put_object(
            bucket_name="arquivos",
            object_name=f"{nome_arquivo}.jpg",
            data=file_stream,
            length=len(downloaded_file)
            )
  
        return f"{nome_arquivo}.jpg"
    except Exception as e:
        print(f"Erro ao salvar no MinIO: {e}", flush=True)
        return None
    
def salvar_audio_bucket(downloaded_file):

    caracteres = string.ascii_letters + string.digits
    nome_arquivo = ''.join(random.choice(caracteres) for _ in range(15))

    # Enviar a imagem diretamente para o Minio
    try:

        from minio import Minio
        load_dotenv()
        
        MINIO_CLIENT = Minio("host.docker.internal:9000", access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)

        # Envia o arquivo para o Minio diretamente da memória sem salvar localmente
        file_stream = io.BytesIO(downloaded_file)

        MINIO_CLIENT.put_object(
            bucket_name="audios",
            object_name=f"{nome_arquivo}.wav",
            data=file_stream,
            length=len(downloaded_file)
            )
  
        # Resposta do bot
        print(f"{nome_arquivo}.wav salvo com sucesso no MinIO!", flush=True)
        return f"{nome_arquivo}.wav"
    except Exception as e:
        print(f"Erro ao salvar no MinIO: {e}", flush=True)
        return None