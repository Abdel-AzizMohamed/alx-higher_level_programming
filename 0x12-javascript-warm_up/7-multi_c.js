#!/usr/bin/node
let i = 0;
if (Number(process.argv[2])) {
  while (process.argv[2] > i) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
