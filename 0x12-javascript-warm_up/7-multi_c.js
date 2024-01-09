#!/usr/bin/node

const args = process.argv;
const x = args[2];
let num = 0;
if (x === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (num < x) {
    console.log('C is fun');
    num++;
  }
}
