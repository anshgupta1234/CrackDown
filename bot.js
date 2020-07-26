const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === 'hey gurl') {
    msg.channel.send('ey dont be a pedo go back to the SAT libtard destroyed lMAO yeet');
  }
});

client.login('NzM2NjYzOTg3NDkxNTY5Njg3.XxyFzQ.zyZdI1-S2tZohyPQnTM6LuE7IQc');