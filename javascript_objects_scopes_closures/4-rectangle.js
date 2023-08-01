#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let xCount = 0;
    let yCount = 0;
    let output = '';
    for (; xCount < this.width; xCount++) {
      output += 'X';
    }
    for (; yCount < this.height; yCount++) {
      console.log(output);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
