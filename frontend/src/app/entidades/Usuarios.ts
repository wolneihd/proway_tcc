export interface Usuario {
  id: number;
  id_telegram: number;
  nome: string;
  sobrenome: string;
  mensagens: Mensagem[];
}

export interface Mensagem {
  id: number;
  texto_msg: string;
  timestamp: number;
  tipo_mensagem: string;
  usuario_id: number; // vai precisar do usuario_id no objeto
  checkbox: boolean;
  nome_arquivo: string;
  analise: Analise;
}

export interface Analise {
  id: number;
  categoria: number;
  erro: string;
  feedback: string;
  llm: string;
  resposta: string;
  resumo: string;
}
