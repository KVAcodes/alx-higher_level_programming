#!/usr/bin/node

exports.esrever = function (list) {
  const tmpArray = [];
  let i = list.length - 1;

  for (; i >= 0; i--) {
    tmpArray.push(list[i]);
  }
  return (tmpArray);
};
