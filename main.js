const mineflayer = require('mineflayer');

const bot = mineflayer.createBot({
  host: 'Voidgamer256.aternos.me',
  port: 45397,
  username: 'Imnotagay'
});

bot.on('spawn', () => {
  console.log('Bot has joined the server.');
  bot.chat('/register humqn52& humqn52&');
  bot.chat('/register humqn52&');
  bot.chat('/login humqn52&');
  bot.chat('Join: https://t.me/Hyper_Speed0');
});

bot.on('chat', (username, message) => {
  if (message === '&leave') {
    if (username === 'OtazukiHS') {
      bot.chat(`${username}, I'm leaving the server. Goodbye!`);
      bot.quit();
    } else {
      bot.chat(`Sorry ${username}, only OtazukiHS can tell me to leave!`);
    }
  }
});

bot.on('error', err => console.log(err));
bot.on('end', () => console.log('Bot disconnected.'));
