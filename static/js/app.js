

$(document).ready(function() {
  var auth = new auth0.WebAuth({
    domain: 'capextool.auth0.com',
    clientID: 'uL61M0bVYCd72QwsrvGioOHotcRlqw35'
   });


  $('.btn-login').click(function(e) {
    e.preventDefault();
    auth.authorize({
      audience: 'https://' + 'capextool.auth0.com' + '/userinfo',
      scope: 'openid profile',
      responseType: 'code',
      redirectUri: AUTH0_CALLBACK_URL
    });
  });

  $('[data-open-details]').click(function (e) {
    e.preventDefault();
    var $tr = $(this).parent();//this will give the tr
    $($tr).next().toggleClass('is-active');
    $($tr).toggleClass('is-active');
  });

  $(".recalc").keyup(function(){
    var tr = $(this).closest('tr');
    var value = tr.find('.val').val();
    var percent = tr.find('.percent').val();

    savings = Math.round(value * percent / 100.0, 2);

    tr.find('#savings').html(savings);

  });
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      $('html, body').animate({
        scrollTop: $(hash).offset().top - 130
      }, 800, function(){

        // Add hash (#) to URL when done scrolling (default click behavior)
        window.location.hash = hash;
      });
    } // End if
  });

  // Add smooth scrolling to all links
  $(".delete-project").on('click', function(event) {

    alert("Whoa there! No deleting this project quite yet, we're working on it though.");

  });

  $(".compare").on('click', function(event) {

    alert("Sorry, unable to compare right now, but we're working on it!");

  });

  $(".export").on('click', function(event) {

    alert("WORD!!");

  });

});




