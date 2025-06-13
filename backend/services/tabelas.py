from sqlalchemy import Column, Integer, String, Text, Boolean, create_engine, ForeignKey, BigInteger
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    sobrenome = Column(String(255), nullable=False)
    id_telegram = Column(BigInteger, nullable=False)

    mensagens = relationship("Mensagem", back_populates="usuario", cascade="all, delete-orphan")

class Mensagem(Base):
    __tablename__ = 'mensagens'

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    tipo_mensagem_id = Column(Integer, ForeignKey('tipos_mensagem.id'), nullable=False)
    
    nome_arquivo = Column(String(255), nullable=True) # link arquivo minio
    texto_msg = Column(Text, nullable=True)
    timestamp = Column(Integer, nullable=False)

    usuario = relationship("Usuario", back_populates="mensagens")
    analise = relationship("AnaliseIA", back_populates="mensagem", uselist=False)
    tipo = relationship("TipoMensagem", back_populates="mensagens")

class AnaliseIA(Base):
    __tablename__ = 'analises_ia'

    id = Column(Integer, primary_key=True)
    mensagem_id = Column(Integer, ForeignKey('mensagens.id'), nullable=False)
    llm_id = Column(Integer, ForeignKey('llm.id'), nullable=True)
    resumo = Column(String(255), nullable=True)
    categoria = Column(String(255), nullable=True)
    feedback = Column(String(255), nullable=True)
    resposta = Column(String(255), nullable=True)
    erro = Column(String(255), nullable=True)

    mensagem = relationship("Mensagem", back_populates="analise")
    llm = relationship("LLM", back_populates="analises")

class LLM(Base):
    __tablename__ = 'llm'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)

    analises = relationship("AnaliseIA", back_populates="llm")

class TipoMensagem(Base):
    __tablename__ = 'tipos_mensagem'

    id = Column(Integer, primary_key=True)
    tipo_mensagem = Column(String(50), nullable=False)

    mensagens = relationship("Mensagem", back_populates="tipo")

class Configs(Base):
    __tablename__ = 'configs'

    id = Column(Integer, primary_key=True)
    llm_selecionada = Column(String(50), nullable=False)
