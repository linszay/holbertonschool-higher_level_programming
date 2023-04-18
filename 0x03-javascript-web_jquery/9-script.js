$(document).ready(function(){
    $.ajax({
      type: "GET",
      url: "https://stefanbohacek.com/hellosalut/?lang=fr",
      success: function(data) {
        $("div#hello").text(data.hello);
      },
      error: function() {
        $("div#hello").text("Error loading translation");
      }
    });
  });
  