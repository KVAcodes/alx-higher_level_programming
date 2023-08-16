#!/usr/bin/node

let argumentNb = 0;

exports.logMe = function (item) {
  console.log(`${argumentNb++} : ${item}`);
};
