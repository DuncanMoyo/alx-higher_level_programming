#!/usr/bin/node

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(parseInt(a) + parseInt(b));
  }
}

const args = process.argv.slice(2);
const num1 = args[0];
const num2 = args[1];

add(num1, num2);
