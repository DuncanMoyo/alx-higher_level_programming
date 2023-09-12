#!/usr/bin/node

const InheritedSquare = require('./5-square');

class Square extends InheritedSquare {
        constructor (size) {
        super(size, size);
        }

	charPrint(c) {
		if (c === undefined) {
			c = 'X';
		}
	}
}

module.exports = Square;
