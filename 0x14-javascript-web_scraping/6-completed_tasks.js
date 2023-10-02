#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    // pass
  }
  const tasks = JSON.parse(body);
  const completedTasks = {};

  for (const task of tasks) {
    if (task.userId in completedTasks) {
      if (task.completed) {
        completedTasks[task.userId.toString()]++;
      }
    } else {
      completedTasks[task.userId.toString()] = 0;
    }
  }
  console.log(completedTasks);
});
