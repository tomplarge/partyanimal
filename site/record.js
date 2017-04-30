function recordDab() {
  var answer = confirm("Ready to see Who's Your Dabby?");
  if (answer) {
    $.ajax({
      url: "../whosyourdabby.py"
      success: function(response) {
      document.getElementById(title).innerHTML = response;
      }


    })
  }



}
