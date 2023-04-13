#!/usr/bin/node

const process = require('process');
const argv = process.argv;

let count = 3;
let biggest = parseInt(argv[2]);
let secondBiggest = 0;

while (count < argv.length) {
  if (argv[count] > biggest) {
    secondBiggest = biggest;
    biggest = parseInt(argv[count]);
  }
  count++;
}

console.log(secondBiggest);
