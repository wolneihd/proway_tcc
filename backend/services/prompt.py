def gerar_prompt(mensagem_usuario: str) -> str:

    prompt = f"""
        1. você deve analisar a mensagem enviada abaixo.
        2. serão 03 respostas que devem ser separadas por ; entre elas para podemos depois podermos tabular os dados.
        3. selecionar somente uma das opções válidas por pergunta.
        - pergunta 01: tipo de feedback: positivo, neutro, negativo
        - pergunta 02: categorizar (somente uma opção válida): atendimento, preço, qualidade, entrega, disponibilidade, pagamento, limpeza, segurança, outro.
        - pergunta 03: resumir em até no máximo 50 caracteres (considerando pontuações e espaços vazios). 

        Feedback do usuário: {mensagem_usuario}. 

        O retorno do assistente deve ser apenas: 

        resposta01;resposta02;resposta03    
        """
    
    return prompt

if __name__ == "__main__":
    gerar_prompt("Achei o atendimento ótimo!")