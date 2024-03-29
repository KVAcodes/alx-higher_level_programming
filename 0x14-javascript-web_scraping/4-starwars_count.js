#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    // pass
  }
  const data = JSON.parse(body);
  const movies = data.results;

  let count = 0;
  movies.forEach((movie) => {
    if (movie.characters.some((str) => str.endsWith('18/'))) {
      count++;
    }
  });
  console.log(count);
});
