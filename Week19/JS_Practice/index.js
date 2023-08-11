
// first_exercise

// var value = prompt("Enter a value:");

// alert(typeof value);


// second_exercise

// var age = prompt("Please enter your age:");

// age = parseInt(age);

// if (age >= 0 && age <= 10) {
//     alert("child");
// }
// else if (age >= 11 && age <= 18) {
//     alert("teenager");
// }
// else if (age >= 19 && age <= 30) {
//     alert("young person");
// }
// else if (age > 30) {
//     alert("adult");
// }


// third_exercise

var username = prompt("Enter your username:")
    document.cookie = "username=" + username;

var cookies = document.cookie.split(';');

for (var i = 0; i < cookies.length; i++) {
    var x = cookies[i].split("=");
    if (x[0] == "username"){
        alert("Hello" + " " + x[1])
    }
}
