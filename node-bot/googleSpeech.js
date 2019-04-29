// [START tts_quickstart]
// Imports the Google Cloud client library
const textToSpeech = require("@google-cloud/text-to-speech");
//const telebot = require("./telebot");

// Import other required libraries
const fs = require("fs");
const util = require("util");

class SpeechGoogle {
  async main(txt) {
    // Creates a client
    const client = new textToSpeech.TextToSpeechClient();

    // The text to synthesize
    const text = txt;

    // Construct the request
    const request = {
      input: { text },
      // Select the language and SSML Voice Gender (optional)
      voice: { languageCode: "pt-BR", ssmlGender: "FEMININO" },
      // Select the type of audio encoding
      audioConfig: { audioEncoding: "MP3" }
    };

    // Performs the Text-to-Speech request
    const [response] = await client.synthesizeSpeech(request);
    // Write the binary audio content to a local file
    const writeFile = util.promisify(fs.writeFile);
    const audio = await writeFile(
      "output.mp3",
      response.audioContent,
      "binary"
    );
    console.log(audio);
    return console.log("Audio content written to file: output.mp3");
  }
}
// [END tts_quickstart]
module.exports = new SpeechGoogle();
