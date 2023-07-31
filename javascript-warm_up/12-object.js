#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
const updatedInfo = {
  value: 89
};
const update = Object.assign({}, myObject, updatedInfo);
console.log(update);
