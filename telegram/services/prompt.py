import requests

def gerar_promt(mensagem_usuario: str) -> str:
    # buscar categorias:
    response = requests.get("http://localhost:8081/categorias")
    categorias = response.json()
    
    # buscar feedbacks:
    # TODO
    feedback = ['positivo', 'neutro', 'negativo']
    
    prompt = f"""
        1. você deve analisar a mensagem enviada abaixo.
        2. serão 03 respostas que devem ser separadas por ; entre elas para podemos depois podermos tabular os dados.
        3. selecionar somente uma das opções válidas por pergunta.
        - pergunta 01: tipo de feedback: {feedback}
        - pergunta 02: categorizar (somente uma opção válida): {categorias}.
        - pergunta 03: resumir em até no máximo 50 caracteres (considerando pontuações e espaços vazios). 

        Feedback do usuário: {mensagem_usuario}. 

        O retorno do assistente deve ser apenas: 

        resposta01;resposta02;resposta03    
        """
    
    print(prompt)
    return prompt

if __name__ == "__main__":
    gerar_promt("Achei o atendimento ótimo!")