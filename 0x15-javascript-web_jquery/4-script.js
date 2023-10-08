$('div#toggle_header').on('click', () => {
    $('header').attr('class', $('header').hasClass('red') ? 'green' : 'red')
});
