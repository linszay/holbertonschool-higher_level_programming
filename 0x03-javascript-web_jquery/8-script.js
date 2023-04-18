$(document).ready(function(){
    $.getJSON("https://swapi-api.hbtn.io/api/films/?format=json", function(data){
      $.each(data.results, function(index, movie){
        $("ul#list_movies").append("<li>" + movie.title + "</li>");
      });
    });
  });
  