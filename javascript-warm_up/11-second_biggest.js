#!/usr/bin/node
const num = process.argv.slice(2);
num.sort((a, b) => b - a);
if (!(num) || !(num[1])) {
  console.log('0');
} else {
  console.log(num[1]);
}
