#!/usr/bin/node

const process = require('process');
const value = parseInt(process.argv[2]);

function fact (val) {
  if (isNaN(val) || val === 1) {
    return (1);
  }
  return (val * fact(val - 1));
}

console.log(fact(value));
