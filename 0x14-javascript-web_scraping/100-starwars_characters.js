#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach((item) => {
    request.get(item, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
