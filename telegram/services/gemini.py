from dotenv import load_dotenv
import os
import google.generativeai as genai
from prompt import gerar_prompt

def analise_texto_gemini(mensagem: str):

    load_dotenv()
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    MODEL = os.getenv('GEMINI_MODEL')

    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(MODEL)

    prompt = gerar_prompt(mensagem)

    response = model.generate_content(prompt)

    # instanciando objeto:
    try:
        texto = response.text
        print('retorno IA: ', response.text)
        # texto = response.choices[0].message.content
        partes = texto.split(';')
        texto_formatado = [parte.replace('"', '').replace('.', '').replace('\n', '') for parte in partes]
        return texto_formatado[0], texto_formatado[1], texto_formatado[2]
    except:
        print("Erro ao gerar Array e instanciar o objeto.")
        return None, None, None

if __name__ == "__main__":
    analise = analise_texto_gemini('Eu não gostei do serviço!')
    print('Retorno IA: ', analise)