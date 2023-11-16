//  Real Time Chat Server Application with Logging Feature
//  ****************************************************** 
//
//  Nov 2022 V3b--dbe --logging output to file added
//  Oct 2022 V3 --dbe --minor corrections
//  Aug 2021 V2 --dbe	--adding logging functionaliyt with timestamp
//  Aug 2021 V1 --dbe	--initial version, debugged from Paul Souvik, Medium Oct'13 2020
//
//  Link
//      https://medium.com/swlh/real-time-chat-application-using-socket-io-in-node-js-37806e98918c
//
import { express } from 'express';
import { createServer } from 'http';

var app = express();
var server = createServer(app);

var io = require('socket.io')(server);
import { join } from 'path';

// --- Timestamp Beautifier
function Timestamp() {
  let date_ob = new Date();

  // current date
  // adjust 0 before single digit date
  let date = ("0" + date_ob.getDate()).slice(-2);

  // current month
  let month = ("0" + (date_ob.getMonth() + 1)).slice(-2);

  // current year
  let year = date_ob.getFullYear();

  // current hours
  let hours = date_ob.getHours();

  // current minutes
  let minutes = date_ob.getMinutes();

  // current seconds
  let seconds = date_ob.getSeconds();

  return year + "-" + month + "-" + date + " " + hours + ":" + minutes + ":" + seconds;
}

// --- LOGGING into files
// get the Console class
import { Console } from "console";
// get fs module for creating write streams
import { createWriteStream } from "fs";

// make a new logger
const myLogger = new Console({
  stdout: createWriteStream("Log-Stdout.txt"),
  stderr: createWriteStream("Log-StdErr.txt"),
});

// --- Logging Message Function
function MsgLog(action, msg) {
	var ts = Timestamp()
    myLogger.log(ts,action,msg);
}


// --- CHAT SERVER Setup and Start 
app.use(join(__dirname,'./public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index2.html');
});


var name;

io.on('connection', (socket) => {
  MsgLog('CONNECT','--- new user connected ${name}');
  
  socket.on('joining msg', (username) => {
  	name = username;
  	io.emit('chat message', `---${name} joined the chat---`);
	MsgLog('ENTER',`--- user [${name}] joined the chat ---`);
  });
  
  socket.on('disconnect', () => {
    MsgLog('EXIT',`--- ${name} left the chat ---`);
    io.emit('chat message', `--- user [${name}] left the chat---`);
    
  });
  socket.on('chat message', (msg) => {
    MsgLog('MESSAGE',`--- user [${name}] send chat message [${msg}] ---`);
    socket.broadcast.emit('chat message', msg);         //sending message to all except the sender
  });
});

server.listen(3000, () => {
  MsgLog('SERVER',`--- ChatRoom Server started listening on port 3000 ---`);
});


