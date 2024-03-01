#!/usr/bin/node

const args = process.argv;
const size = args[2];
let num = 0;

if (size === undefined || isNaN(size)) {
  console.log('Missing size');
} else {
  while (num < size) {
    console.log('X'.repeat(size));
    num++;
  }
}
