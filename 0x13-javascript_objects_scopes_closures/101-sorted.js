#!/usr/bin/node

const dict = require('./101-data.js');

const rslt = {};
const entries = dict.dict;

for (const k in entries) {
  const occurrence = entries[k];

  if (rslt[occurrence] === undefined) {
    rslt[occurrence] = [k];
  } else {
    rslt[occurrence].push(k);
  }
}

console.log(rslt);
