'use strict';
var bodyParser = require('body-parser');
var app = require("express")();
var http = require("http").Server(app);
var io = require("socket.io")(http);


module.exports = function(app) {
    app.get('/', function(req, res) {
        res.render('pages/index');
    });

    app.get('/data', function(req, res) {
        res.render('pages/data');
    });

    app.use(bodyParser.urlencoded({
    	extended: true
    }));

    app.use(bodyParser.text())

    app.post('/data', function(req, res) {
        res.render('pages/data');
        // do something with the datum
        console.log(req.body)


        var htmlsource = fs.readFileSync('data.ejs','utf-8');
        var $ = window.$
        var title = $("title").text()
        $('#sanqrooth').text(title);

        console.log(documentToSource(window.document))

    });
};
