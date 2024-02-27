$(document).ready(function () {
    $('#sort-form').submit(function (event) {
        event.preventDefault();  // Предотвращение стандартного поведения формы

        console.log('Button clicked');


        var form = $(this);
        var year = form.serializeArray()[0].value;
        var director = form.serializeArray()[1].value;
        var actor = form.serializeArray()[2].value;
        $.ajax({
            url: '/api/movie/list/',  // Указание URL для вашего API
            method: 'GET',
            data: [{"name":"year","value":year},{"name":"directors__name","value":director},{"name":"actors__name","value":actor}],
            dataType: 'json',
            success: function (data) {
                console.log('Data received:', data);
                displayMovies(data);
                console.log('Data sent:', JSON.stringify(form.serializeArray()));
            },
            error: function (error) {
                console.log('Error:', error);
            }
        });
    });


    function displayMovies(movies) {
        console.log('Displaying movies:', movies);

        var movieListDiv = $('#movie-list');
        movieListDiv.empty();

        if (movies.length === 0) {
            movieListDiv.append('<p>No movies found.</p>');
        } else {
            var ul = $('<ul>');
            movies.forEach(function (movie) {
                var li = $('<li class="clickable" data-movie-id="' + movie.id + '">' + movie.title + ' (' + movie.year + ')</li>');
                ul.append(li);
            });
            movieListDiv.append(ul);

            // Add click event handler after appending to the DOM
            ul.on('click', 'li.clickable', function() {
                var movieId = $(this).data('movie-id');
                var movieDetailUrl = '/movie/' + movieId + '/';  // Replace with your actual URL pattern
                window.location.href = movieDetailUrl;
            });
        }
    }
});
