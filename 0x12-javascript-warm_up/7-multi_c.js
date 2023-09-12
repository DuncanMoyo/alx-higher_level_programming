#!/usr/bin/node

const args = process.argv.slice(2);
const x = parseInt(args[0]);

let i;

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
