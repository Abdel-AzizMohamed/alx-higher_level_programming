#!/usr/bin/node
const fs = require('fs');

fs.read(process.argv[2], 'utf-8', function (err, data) {
  console.log(err || data.toString());
});
