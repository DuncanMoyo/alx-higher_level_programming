#!/usr/bin/node

const request = require('request');
const process = require('process');

let url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});

