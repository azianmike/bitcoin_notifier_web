function register(){
    if(document.getElementById("password").value == document.getElementById("confirmPassword").value){
        var paramsJSON = {};
        paramsJSON['email'] = document.getElementById("email").value;
        paramsJSON['password'] = hashPassword(document.getElementById("password").value);
        postToUrl("/registerJSON/", paramsJSON);
    } else {
        alert("The passwords that you entered do not match!");
    }
}


