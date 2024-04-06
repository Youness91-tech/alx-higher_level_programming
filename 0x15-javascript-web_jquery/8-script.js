// avaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response) {
  for (const movie of response.results) {
    $('UL#list_movies').append(`<li>${movie.title}</li>`);
  }
});
