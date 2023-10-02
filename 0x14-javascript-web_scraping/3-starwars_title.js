#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    // pass
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
