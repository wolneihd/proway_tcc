from dotenv import load_dotenv
import os
import google.generativeai as genai
from services.prompt import gerar_prompt

def analise_texto_gemini(mensagem: str):

    try:
        load_dotenv()
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        MODEL = os.getenv('GEMINI_MODEL')

        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel(MODEL)

        prompt = gerar_prompt(mensagem)
        response = model.generate_content(prompt)

        texto = response.text
        texto = response.choices[0].message.content
        partes = texto.split(';')
        texto_formatado = [parte.replace('"', '').replace('.', '').replace('\n', '') for parte in partes]
        return texto_formatado[0], texto_formatado[1], texto_formatado[2], None
    except Exception as e:
        if "429 You exceeded your current quota" in str(e):
            erro = "Limite de Tokens do Gemini excedido. Verificar com o suporte."
            print(erro, flush=True)
            return None, None, None, erro
        else:
            print(f"Erro na analise do Gemini {e}", flush=True)
            texto_curto_255_char = e[:255]
            return None, None, None, texto_curto_255_char

if __name__ == "__main__":
    analise = analise_texto_gemini('Eu não gostei do serviço!')
    print('Retorno IA: ', analise)