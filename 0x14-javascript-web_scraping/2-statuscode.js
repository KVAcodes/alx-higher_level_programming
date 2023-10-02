#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    // pass
  }
  console.log('code:', response.statusCode);
});
