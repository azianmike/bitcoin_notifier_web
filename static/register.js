function register(){
    if(document.getElementById("password").value == document.getElementById("confirmPassword").value){
        var paramsJSON = {};
        paramsJSON['email'] = document.getElementById("email").value;
        paramsJSON['password'] = hashPassword(document.getElementById("password").value);
        postToUrl("/registerJSON/", paramsJSON, registerCallback);
    } else {
        alert("The passwords that you entered do not match!");
    }
}

function registerCallback(jsonData){
        if(jsonData["success"] == "1"){
          // this means the user has been registere
          alert("Success!");
          window.location.replace("/");
          } else if(jsonData["success"] == "0"){
            alert("Error: Email is already registered");
          } else {
            alert("Fatal error");
        }



}
