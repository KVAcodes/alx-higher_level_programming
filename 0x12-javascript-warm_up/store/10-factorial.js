#!/usr/bin/node

const process = require('process');
const argv = process.argv;

const num = parseInt(argv[2]);

function fact (num) {
  if (isNaN(num)) {
    return (1);
  }
  if (num === 2) {
    return (num);
  }
  return (num * fact(num - 1));
}

console.log(fact(num));
