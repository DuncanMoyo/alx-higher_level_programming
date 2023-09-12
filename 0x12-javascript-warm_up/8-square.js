#!/usr/bin/node

const args = process.argv.slice(2);
const size = parseInt(args);

let line = '';

if (!isNaN(size)) {
  if (size > 0) {
    for (let i = 0; i < size; i++) {
      for (let j = 0; j < size; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }
} else {
  console.log('Missing size');
}
