// $(document).ready(function() {
//   var auth = new auth0.WebAuth({
//     domain: AUTH0_DOMAIN,
//     clientID: AUTH0_CLIENT_ID
//    });


//     $('.btn-login').click(function(e) {
//       e.preventDefault();
//       auth.authorize({
//         audience: 'https://'+AUTH0_DOMAIN+'/userinfo', // you can also set this on the .env file and put API_AUDIENCE instead
//         scope: 'openid profile',
//         responseType: 'code',
//         redirectUri: AUTH0_CALLBACK_URL
//       }); 
//     });
    
//     $('.btn-logout').click(function(e) {
//       e.preventDefault();
//       window.location.href = '/logout';
//     });
// });

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
        redirectUri: 'http://127.0.0.1:5000/callback'
      });
    });
});  