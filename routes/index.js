'use strict';

module.exports = function(app) {
    app.get('/', function(req, res) {
        res.render('pages/index');
    });

    app.get('/data', function(req, res) {
        res.render('pages/data');
    });
};