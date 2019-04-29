# NODE_TELEBOT

---

#Sobre:
Projeto que faz integração a API do node-telegram-bot-api com a API text-to-speech da google. Tem como objetivo pegar o que foi escrito no telegram apos digitar os comandos que foi configurado na api e transformar em voz

---

## Iniciando projeto

1. Criando projeto: yarn init -y

2. Instalando as dependencias usadas nesse projeto:

- "@google-cloud/text-to-speech": "^0.5.1",
- "dotenv": "^7.0.0",
- "eslint": "^5.16.0",
- "node-telegram-bot-api": "^0.30.0",
- "nodemon": "^1.18.11",

3. Criando um script para start do nodemon:

```
"scripts": {
  "start": "nodemon index.js"
}
```
