$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: "GET",
    dataType: "json",
    success: function(response) {
          $('div#character').text(response.name);
        },
    error: function(xhr, status, error) {
          console.error(status, error);
        }
});
