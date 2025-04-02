const fs = require('fs');
const readline = require('readline');
const EventEmitter = require('events');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const eventEmitter = new EventEmitter();
eventEmitter.on('textReady', (text) => {
  console.log(`Custom event fired: Text is ready - ${text}`);
  fs.writeFile('text.txt', text, (err) => {
    if (err) throw err;
    console.log('Text has been saved to text.txt');
    rl.close();
  });
});
rl.question('Enter some text: ', (text) => eventEmitter.emit('textReady', text));