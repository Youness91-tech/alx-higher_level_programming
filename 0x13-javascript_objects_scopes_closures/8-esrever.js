#!/usr/bin/node

exports.esrever = function (list) {
  let num = list.length - 1;
  const newList = [];

  while (num >= 0) {
    newList.push(list[num]);
    num--;
  }

  return newList;
};
