import requests
from services.groq_ia import analise_texto_gropIA
from datetime import datetime, timezone

class Mensagem:
    def __init__(self, user, endereco_arquivo: str = None, transcricao_audio: str = None): 
        self.id_Telegram = user.from_user.id  
        self.nome = user.from_user.first_name  
        self.sobrenome = user.from_user.last_name if user.from_user.last_name else ''  
        self.tipo_mensagem = None
        self.respondido = False
        self.textoMensagem = None
        self.caminhoArquivo = None
        self.resposta = None
        self.horario_envio = datetime.fromtimestamp(user.date, tz=timezone.utc)
        self.llm = self.buscar_llm_configurada()
        
        # após análise:
        self.feedback = None
        self.categoria = None
        self.resumo = None
        self.resposta = None
        
        self.buscar_llm_configurada()
        self.information_por_tipo_dado(user, endereco_arquivo, transcricao_audio)
        
    def information_por_tipo_dado(self, data: dict, endereco_arquivo: str = None, transcricao_audio: str = None):
        if (data.content_type) == "text":
            self.textoMensagem = data.json['text']
            self.tipo_mensagem = "TEXTO"
            self.analise_ia()
        elif (data.content_type) == "photo":
            self.caminhoArquivo = endereco_arquivo
            self.tipo_mensagem = "IMAGEM"
        elif (data.content_type) == "voice":
            self.textoMensagem = transcricao_audio
            self.caminhoArquivo = endereco_arquivo
            self.tipo_mensagem = "AUDIO"
            self.analise_ia()
           
    def analise_ia(self):
        self.feedback, self.categoria, self.resumo = analise_texto_gropIA(self.textoMensagem)
        
    def buscar_llm_configurada(self) -> str | None:
        response = requests.get("http://localhost:8081/configs")
        obj = response.json()
        if (obj):
            return obj.get('llm')
        else:
            return None
    
    def salvar_dados_banco_dados(self):
        mensagem = {
            "idTelegram": self.id_Telegram,
            "nome": self.nome,
            "sobrenome": self.sobrenome,
            "mensagens": [
                {
                    "tipoMensagem": self.tipo_mensagem,
                    "respondido": self.respondido,
                    "textoMensagem": self.textoMensagem,
                    "caminhoArquivo": self.caminhoArquivo,
                    "resposta": self.resposta,
                    "instant": self.horario_envio,
                    "analise": {
                        "llm": self.llm,
                        "feedback": self.feedback,
                        "categoria": self.categoria,
                        "resumo": self.resumo,
                        "resposta": self.resposta
                    }
                }
            ]
        }
        response = requests.post("http://localhost:8081/", json=mensagem)
        response.json()
        print(f"Salvando o objeto: {response}")
    
