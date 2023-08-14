#!/usr/bin/node

let sortedSlice = process.argv.slice(2, process.argv.length);
if (sortedSlice.length < 2) {
  console.log(0);
} else {
  sortedSlice = sortedSlice.sort((a, b) => a - b);
  console.log(sortedSlice[sortedSlice.length - 2]);
}
