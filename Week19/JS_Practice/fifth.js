function rememberMe() {
    var rememberCheckbox = document.getElementById("rememberCheckbox");
    var usernameInput = document.getElementById("usernameInput");
    
    if (rememberCheckbox.checked) {
      document.cookie = "username=" + usernameInput.value
    }
  }
  
function checkCookie() {
    var usernameInput = document.getElementById("usernameInput");

    var cookies = document.cookie.split(';');

    for (var i = 0; i < cookies.length; i++) {
        var x = cookies[i].split("=");
        if (x[0] == "username"){
            usernameInput.value = x[1];
            break
        }
    }
}

checkCookie();


