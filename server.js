'use strict';

// ================================================================
// get all the tools we need
// ================================================================
var express = require('express');
var routes = require('./routes/index.js');
var port = process.env.PORT || 3000;

var app = express();

// ================================================================
// setup our express application
// ================================================================
app.use('views', express.static(process.cwd() + 'views'));
app.use(express.static( __dirname + '/public'));
app.use(express.static(__dirname + '/screenshots'));
app.set('view engine', 'ejs');


// ================================================================
// setup routes
// ================================================================
routes(app);

// ================================================================
// start our server
// ================================================================
app.listen(port, function() {
    console.log('Server listening on port ' + port + '...');
});