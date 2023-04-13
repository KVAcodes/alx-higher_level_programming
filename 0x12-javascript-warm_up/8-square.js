#!/usr/bin/node

const process = require('process');
const argv = process.argv;

const num = parseInt(argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
    for (let x = 0; x < num; x++) {
      console.log('X'.repeat(num));
  }
}
