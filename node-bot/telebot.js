const Telebot = require("node-telegram-bot-api");

const token = process.env.TELEGRAN_API_KEY;
const bot = new Telebot(token, { polling: true });
const googleSpeech = require("./googleSpeech");

const startBot = new RegExp(/start/);
const sayBot = new RegExp(/say/);

const response = () => {
  bot.onText(startBot, async msg => {
    await googleSpeech.main("Bot iniciado com sucesso");
    bot.sendVoice(msg.chat.id, "./output.mp3");
  });

  bot.onText(sayBot, async msg => {
    const texto = msg.text;
    await googleSpeech.main(texto.slice(5, -1));
    bot.sendVoice(msg.chat.id, "./output.mp3");
  });

  bot.on("new_chat_members", async msg => {
    const texto = `Ola seja bem vindo ${
      msg.new_chat_participant.first_name
    } ao melhor grupo do mundo`;
    await googleSpeech.main(texto);
    bot.sendVoice(msg.chat.id, "./output.mp3");
  });
};
bot.on("polling_error", err => console.log(err));
module.exports = response();
