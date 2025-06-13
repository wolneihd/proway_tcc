from services.groq_ia import analise_texto_gropIA
from services.gemini import analise_texto_gemini
from services.chatGPT import analise_texto_chatgpt
from services.repositorio import Database
from datetime import datetime, timezone

class Mensagem:
    def __init__(self, user, endereco_arquivo: str = None, transcricao_audio: str = None): 

        # Usuario
        self.id_Telegram = None
        self.nome = None
        self.sobrenome = None

        # Mensagem  
        self.nome_arquivo = None
        self.textoMensagem = None
        self.horario_envio = None # Timestamp        
        self.tipo_mensagem = None
        self.resposta = None        
        
        # Analise IA:
        self.llm = None
        self.resumo = None
        self.categoria = None
        self.feedback = None   
        self.resposta = None
        self.erro = None

        # processamento das informações (regras de negócio):
        self.db = Database()
        self.llm = self.db.buscar_llm_disponivel()
        self.informacoes_usuario(user)
        self.information_por_tipo_dado(user, endereco_arquivo, transcricao_audio)
        self.obter_horario_envio(user)

        # salvando no Banco de Dados:
        self.nova_mensagem = self.to_dict()
        self.response = self.db.salvar_nova_mensagem(self.nova_mensagem)
        self.db.encerrar_sessao()

    def informacoes_usuario(self, user):
        try:
            self.id_Telegram = user.from_user.id  
            self.nome = user.from_user.first_name  
            self.sobrenome = user.from_user.last_name if user.from_user.last_name else ''
        except Exception as e:
            print(f"Erro ao pegar dados do usuario: {e}")

    def information_por_tipo_dado(self, data: dict, endereco_arquivo: str = None, transcricao_audio: str = None):
        try:
            if (data.content_type) == "text":
                self.textoMensagem = data.json['text']
                self.tipo_mensagem = "texto"
                self.analise_ia()
            elif (data.content_type) == "photo":
                self.caminhoArquivo = endereco_arquivo
                self.tipo_mensagem = "imagem"
            elif (data.content_type) == "voice":
                self.textoMensagem = transcricao_audio
                self.caminhoArquivo = endereco_arquivo
                self.tipo_mensagem = "audio"
                self.analise_ia()
        except Exception as e:
            print(f"Erro ao pegar dados da Mensagem: {e}")
           
    def obter_horario_envio(self, data):
        try:
            self.horario_envio = data.date
            self.datetime_envio = datetime.fromtimestamp(data.date, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        except Exception as e:
            self.datetime_envio = None
            print(f"Erro ao obter Timestamp e converter para DateTime: {e}", flush=True)

    def analise_ia(self):
        if self.llm == "GroqIA":
            self.feedback, self.categoria, self.resumo, self.erro = analise_texto_gropIA(self.textoMensagem)
        elif self.llm == "Gemini":
            self.feedback, self.categoria, self.resumo, self.erro = analise_texto_gemini(self.textoMensagem)
        elif self.llm == "ChatGPT":
            self.feedback, self.categoria, self.resumo, self.erro = analise_texto_chatgpt(self.textoMensagem)
        
    def to_dict(self):
        return {
                "id_Telegram": self.id_Telegram,
                "nome": self.nome,
                "sobrenome": self.sobrenome,
                "nome_arquivo": self.nome_arquivo,
                "textoMensagem": self.textoMensagem,
                "horario_envio": self.horario_envio,
                "datetime_envio": self.datetime_envio,
                "tipo_mensagem": self.tipo_mensagem,
                "resposta": self.resposta,
                "llm": self.llm,
                "resumo": self.resumo,
                "categoria": self.categoria,
                "feedback": self.feedback,
                "erro": self.erro
            }

    def retorno_usuario(self):
        if self.response:
            return "Sua mensagem foi recebida e estaremos analisando."
        else:
            return "Infelizmente houve problema no processamento da sua mensagem. Favor tentar mais tarde."