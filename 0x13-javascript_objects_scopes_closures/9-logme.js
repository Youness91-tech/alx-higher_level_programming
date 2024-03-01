#!/usr/bin/node

let argsCounter = 0;

exports.logMe = function (item) {
  console.log(`${argsCounter}: ${item}`);
  argsCounter++;
};
