import os
import mysql.connector;
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, selectinload
from services.tabelas import Usuario, AnaliseIA, LLM, TipoMensagem, Base, Configs, Mensagem

class Database:
    def __init__(self):
        load_dotenv()
        self.USER = os.getenv('USER')
        self.PASSWORD = os.getenv('PASSWORD')
        self.DATABASE = os.getenv('DATABASE')
        self.PORT = os.getenv('PORT')  
        self.HOST = os.getenv('HOST')
        self.DATABASE_URL = f"mysql+mysqlconnector://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}"

        self.imprimir_string_conexão()

        self.engine = create_engine(self.DATABASE_URL, pool_pre_ping=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def imprimir_string_conexão(self):
        print(self.DATABASE_URL, flush=True)

    def criar_database_se_nao_existir(self):
        try:
            conexao = mysql.connector.connect(
                host=self.HOST,
                port=self.PORT,
                user=self.USER,
                password=self.PASSWORD,
                )
            cursor = conexao.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.DATABASE};")
            print('Database criado/já existente.', flush=True)
        except Exception as e:
            print(f'Erro ao criar database {self.DATABASE}: {e}', flush=True)
        finally:
            conexao.close()

    def criar_tabelas(self):
        try:
            print("Criando as tabelas no banco de dados...", flush=True)
            Base.metadata.create_all(self.engine)
            print("Tabelas criadas com sucesso!", flush=True)
        except Exception as e:
            print(f"Error creating tables: {e}")

    def migracao_dados(self):
        try:
            # verificando se as tabelas LLM e TIPO_MENSAGEM estão vazias
            valores_tabela_llm = self.session.query(LLM).count()
            valores_tabela_tipo_mensagem = self.session.query(TipoMensagem).count()
            valores_tabela_config = self.session.query(Configs).count()

            if not valores_tabela_llm:
                llms = [
                    LLM(nome="GroqAI"),
                    LLM(nome="ChatGPT"),
                    LLM(nome="Gemini"),
                ]
                self.session.add_all(llms)
                self.session.commit()
            else: 
                print(f"Tabela LLM já possui dados. Migração não necessária", flush=True)

            if not valores_tabela_tipo_mensagem:
                tipos_mensagem = [
                    TipoMensagem(tipo_mensagem="texto"),
                    TipoMensagem(tipo_mensagem="audio"),
                    TipoMensagem(tipo_mensagem="imagem"),
                ]
                self.session.add_all(tipos_mensagem)
                self.session.commit()
            else: 
                print(f"Tabela TipoMensagem já possui dados. Migração não necessária", flush=True)  

            if not valores_tabela_config:
                config_inicial = [
                    Configs(llm_selecionada="GroqAI"),
                ]
                self.session.add_all(config_inicial)
                self.session.commit()
            else: 
                print(f"Tabela Configs já possui dados. Migração não necessária", flush=True)            

        except Exception as e:
            self.session.rollback()
            print(f"Erro na migração dos dados: {e}")

    def buscar_llm_disponivel(self) -> str | None:
        try:
            configs = self.session.query(Configs).first()
            return configs.llm_selecionada
        except Exception as e:
            print(f"Erro ao buscar LLM: {e}")
            return None

    def salvar_nova_mensagem(self, data: dict) -> bool:
        try:            
            # Busca ou cria usuário
            usuario = self.session.query(Usuario).filter_by(id_telegram=data.get('id_Telegram')).first()
            if not usuario:
                usuario = Usuario(
                    nome=data.get('nome'),
                    sobrenome=data.get('sobrenome'),
                    id_telegram=data.get('id_Telegram')
                )
                self.session.add(usuario)
                self.session.commit()  # Necessário para obter o ID

            # Busca tipo de mensagem e LLM
            tipo_mensagem = self.session.query(TipoMensagem).filter_by(tipo_mensagem=data.get('tipo_mensagem')).first()
            if not tipo_mensagem:
                return False

            llm_selected = self.session.query(LLM).filter_by(nome=data.get('llm')).first()
            if not llm_selected:
                return False

            # Cria mensagem
            nova_mensagem = Mensagem(
                usuario_id=usuario.id,
                tipo_mensagem_id=tipo_mensagem.id,
                nome_arquivo=data.get('nome_arquivo'),
                texto_msg=data.get('textoMensagem'),
                timestamp=data.get('horario_envio')
            )
            self.session.add(nova_mensagem)
            self.session.commit()  # Para obter nova_mensagem.id

            # Cria análise vinculada à nova mensagem
            nova_analise_ia = AnaliseIA(
                mensagem_id=nova_mensagem.id,
                llm_id=llm_selected.id,
                resumo=data.get('resumo'),
                categoria=data.get('categoria'),
                feedback=data.get('feedback'),
                resposta=data.get('resposta'),
                erro=data.get('erro')
            )
            self.session.add(nova_analise_ia)
            self.session.commit()

            return True

        except Exception as e:
            print(f"Erro ao inserir nova mensagem no banco: {e}")
            self.session.rollback()
            return False        
  
    def encerrar_sessao(self):
        self.session.close()

    # Essa parte foi gerada com IA (primeiros testes com sucesso)
    def buscar_todos_usuarios_em_dict(self):
        try:
            usuarios = (
                self.session.query(Usuario)
                .options(
                    selectinload(Usuario.mensagens)
                    .selectinload(Mensagem.analise),
                    selectinload(Usuario.mensagens)
                    .selectinload(Mensagem.tipo)
                )
                .all()
            )

            resultado = []
            for usuario in usuarios:
                resultado.append({
                    "id": usuario.id,
                    "nome": usuario.nome,
                    "sobrenome": usuario.sobrenome,
                    "id_telegram": usuario.id_telegram,
                    "mensagens": [
                        {
                            "id": mensagem.id,
                            "nome_arquivo": mensagem.nome_arquivo,
                            "texto_msg": mensagem.texto_msg,
                            "timestamp": mensagem.timestamp,
                            "tipo_mensagem": mensagem.tipo.tipo_mensagem if mensagem.tipo else None,
                            "analise": {
                                "id": mensagem.analise.id if mensagem.analise else None,
                                "resumo": mensagem.analise.resumo if mensagem.analise else None,
                                "categoria": mensagem.analise.categoria if mensagem.analise else None,
                                "feedback": mensagem.analise.feedback if mensagem.analise else None,
                                "resposta": mensagem.analise.resposta if mensagem.analise else None,
                                "erro": mensagem.analise.erro if mensagem.analise else None,
                                "llm": mensagem.analise.llm.nome if mensagem.analise and mensagem.analise.llm else None
                            } if mensagem.analise else None
                        } for mensagem in usuario.mensagens
                    ]
                })

            return resultado
        
        except Exception as e:
            print(f"Erro ao buscar todos os usuários: {e}")
            None
        
        


