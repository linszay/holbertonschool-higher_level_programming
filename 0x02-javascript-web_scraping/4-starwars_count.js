#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(`${apiUrl}?format=json`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Unexpected status code: ${response.statusCode}`);
    return;
  }

  const movies = JSON.parse(body).results;
  const wedgeMovies = movies.filter(movie =>
    movie.characters.some(characterUrl => characterUrl.includes(`/${characterId}/`))
  );

  console.log(`${wedgeMovies.length}`);
});
