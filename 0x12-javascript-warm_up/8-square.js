#!/usr/bin/node

const process = require('process');
const value = parseInt(process.argv[2]);
let count = 0;

if (isNaN(value)) {
  console.log('Missing size');
} else {
  for (; count < value; count++) {
    console.log('X'.repeat(value));
  }
}
