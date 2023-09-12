#!/usr/bin/node

//  Function thatprints the number of arguments printed and new argument value
let numOfArgPrinted = -1;
exports.logMe = function (item) {
  numOfArgPrinted++;
  console.log(numOfArgPrinted + ': ' + item);
};
