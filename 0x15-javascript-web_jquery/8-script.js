$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: "GET",
    dataType: "json",
    success: function(response) {
          response.results.forEach(function(movie) {
                  $('ul#list_movies').append('<li>' + movie.title + '</li>');
                });
        },
    error: function(xhr, status, error) {
          console.error(status, error);
        }
});
