// SignIn / Register Toggle

function hideLoginForm(elm=null){
    $('.login-form').hide()
    $('.register-form').show()
    $(".formHeading").text("Register")
  }

function hideSignupForm(elm=null){
      $('.register-form').hide()
      $('.login-form').show()
      $(".formHeading").text("Login")
  }

// Events
$('.login-form .message a').click(function(){
    $('.login-form').hide()
    $('.register-form').animate({height: "toggle", opacity: "toggle"}, "slow");
    $(".formHeading").text("Register")
 });
$('.register-form .message a').click(function(){
    $('.register-form').hide()
    $('.login-form').animate({height: "toggle", opacity: "toggle"}, "slow");
    $(".formHeading").text("Login")
 });


 function googleTranslateElementInit() {
    new google.translate.TranslateElement({pageLanguage: 'en', layout: google.translate.TranslateElement.FloatPosition.TOP_LEFT}, 'google_translate_element');
  }

