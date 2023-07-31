#!/usr/bin/node
const argsText = process.argv.slice(2);

if (argsText[0]) {
  console.log(argsText[0]);
} else {
  console.log('No argument');
}

