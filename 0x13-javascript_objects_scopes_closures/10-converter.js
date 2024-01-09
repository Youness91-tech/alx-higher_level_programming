#!/usr/bin/node

exports.converter = function (base) {
  return function converterFunc (number) {
    return number.toString(base);
  };
};
