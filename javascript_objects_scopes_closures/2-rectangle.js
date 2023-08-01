#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.with = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
