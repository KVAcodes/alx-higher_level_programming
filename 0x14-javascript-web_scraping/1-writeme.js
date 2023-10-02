#!/usr/bin/node

const process = require('process');
const fs = require('fs');
const filePath = process.argv[2];
const data = process.argv[3];

fs.writeFile(filePath, data, (err) => {
  if (err) {
    console.error(err);
  }
});
