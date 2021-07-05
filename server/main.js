var config = require('./common/config');
var express = require('express');
var cors = require('cors');
var http = require('http');
var logger = require('./common/logger').createLogger(); // logs to STDOUT

// Warm up
if(config.debug_mode) {
    // logger = require('./common/logger').createLogger('./logs/deugger_'+Date.now()+'.log');
    logger.setLevel('debug');
    logger.log('NB : This is DEBUG mode only, files will be stored in play JSON.');
}

// TODO: create bootstrap to clean this up
var app = express();
app.use(cors());

// Angular transpiled dir
app.use(express.static(__dirname + '/client/dist'));

app.get('/', ((req, res)=> {
    res.status(500).send('Okay boomer.');
}));

// Start
app.listen(config.connections.entry.port, (()=>{
    logger.log('Listening on port: ' + config.connections.entry.port);
}))