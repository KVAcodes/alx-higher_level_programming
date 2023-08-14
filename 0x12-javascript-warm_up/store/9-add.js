#!/usr/bin/node

const process = require('process');
const argv = process.argv;

const num1 = parseInt(argv[2]);
const num2 = parseInt(argv[3]);

function add (a, b) {
  return (a + b);
}

console.log(add(num1, num2));
