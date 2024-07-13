#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  const movie_id = process.argv[2];

  request(`https://swapi-api.alx-tools.com/api/films/${movie_id}`, async function (error, response, body) {
    if (error) {
      console.error('Error making GET request:', error);
    } else if (response.statusCode !== 200) {
      console.error('Failed to get data:', response.statusCode);
    } else {
      const link_list = JSON.parse(body).characters;
      await fetchNames(link_list);
    }
  });

}

async function fetchNames(links) {

  for (const link of links) {
    await new Promise((resolve, reject) => {
      request(link, (err, res, body) => {
        if (err) {
          return reject(err);
        }

        const value = JSON.parse(body);
        console.log(value.name);
        resolve();
      });
    });
  }

}