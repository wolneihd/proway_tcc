import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import RateLimitError
import openai
from services.prompt import gerar_prompt
# from prompt import gerar_prompt

def analise_texto_chatgpt(mensagem: str):

    try:
        load_dotenv()
        OPEN_AI_KEY = os.getenv('OPENAI_API_KEY')
        OPENAI_MODEL = os.getenv('OPENAI_MODEL')

        if (OPEN_AI_KEY == None or OPENAI_MODEL == None):
            return None, None, None, "ChatGPT não tem Chave API_KEY registrada para análise dos feedbacks."

        prompt = gerar_prompt(mensagem)

        messages = [
            {"role": "system", "content": "Você é um assistente que recebe um prompt de um agente e deve retornar conforme desejado."},
            {"role": "user", "content": prompt}
        ]

        client = openai.OpenAI(api_key=OPEN_AI_KEY)
        chat_completion = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            temperature=1,
            max_tokens=None,
            timeout=None,
        )

        analise = chat_completion.choices[0].message['content']
        partes = analise.split(';')
        texto_formatado = [parte.replace('"', '').replace('.', '').replace('\n', '') for parte in partes]
        return texto_formatado[0], texto_formatado[1], texto_formatado[2], None

    except Exception as error:
        print(f'Erro ao enviar para análise do ChatGPT: {error}', flush=True)
        return None, None, None, "Erro ao enviar para análise do ChatGPT"

if __name__ == "__main__":
    analise = analise_texto_chatgpt('Eu não gostei do serviço!')
    print('Retorno IA: ', analise)