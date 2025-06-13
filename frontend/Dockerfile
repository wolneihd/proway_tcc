FROM node:alpine

WORKDIR /usr/src/app

# Copiar todos os arquivos do diretório atual para o contêiner
COPY . /usr/src/app

# Instalar o Angular CLI globalmente
RUN npm install -g @angular/cli

# Instalar as dependências do projeto
RUN npm install

# Expor a porta 4200
EXPOSE 4200

# Iniciar o servidor Angular, escutando em todas as interfaces
CMD ["ng", "serve", "--host", "0.0.0.0", "--port", "4200"]
