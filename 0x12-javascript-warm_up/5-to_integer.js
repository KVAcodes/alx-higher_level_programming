#!/usr/bin/node

const process = require('process');
const value = parseInt(process.argv[2]);

console.log(isNaN(value) ? 'Not a number' : 'My number: ' + value);
