#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
const updateInfo = {
  value: 89
};
const update = Object.assign({}, myObject, updatedInfo);
console.log(update);
