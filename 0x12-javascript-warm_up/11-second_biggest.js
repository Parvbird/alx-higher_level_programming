#!/usr/bin/node

// destructuring array to remove first two arguments
const [, , ...args] = process.argv;

if (args.length < 2) {
  console.log(0);
} else {
  const sortedNumbers = args.sort((a, b) => b - a);
  const secondLargest = sortedNumbers[1];

  console.log(secondLargest);
}
