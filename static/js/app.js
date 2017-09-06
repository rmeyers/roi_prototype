

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

});




