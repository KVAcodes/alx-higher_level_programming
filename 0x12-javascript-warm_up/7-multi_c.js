#!/usr/bin/node

const process = require('process');
let count = 0;

if (process.argv[2]) {
  for (; count < process.argv[2]; count++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
