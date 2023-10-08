$(function() {
  api_url = 'https://hellosalut.stefanbohacek.dev/';
  $('input#btn_translate').click(function() {
    $.ajax({
      url: api_url + '?' + 'lang=' + $('input#language_code').val(),
      method: "GET",
      dataType: "json",
      success: function(response) {
        $('div#hello').html(response.hello);
      },
      error: function(xhr, status, error) {
        console.error(status, error);
      }
    });
  });
  $('input#language_code').on('keyup', function(event) {
    if (event.keyCode === 13) {
      $.ajax({
        url: api_url + '?' + 'lang=' + $('input#language_code').val(),
        method: "GET",
        dataType: "json",
        success: function(response) {
          $('div#hello').html(response.hello);
        },
        error: function(xhr, status, error) {
          console.error(status, error);
        }
      });
    }
  });
});
