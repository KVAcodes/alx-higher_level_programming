#!/usr/bin/node

const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    let i = 0;
    for (; i < this.height; i++) {
      console.log(c ? c.repeat(this.width) : 'X'.repeat(this.width));
    }
  }
};
