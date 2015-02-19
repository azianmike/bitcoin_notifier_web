function register(){
    if(document.getElementById("password").value == document.getElementById("confirmPassword").value){
        var paramsJSON = {};

        paramsJSON['email'] = document.getElementById("email").value;
        if (validateEmail(paramsJSON['email']){
          alert("Email is not valid");
          return;
        }
        paramsJSON['password'] = hashPassword(document.getElementById("password").value);
        postToUrl("/registerJSON/", paramsJSON, registerCallback);
    } else {
        alert("The passwords that you entered do not match!");
    }
}

function validateEmail(email) { 
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
} 

function registerCallback(jsonData){
        if(jsonData["success"] == "1"){
          // this means the user has been registere
            showAlertMessage(jsonData["message"]);            
          } else if(jsonData["success"] == "0"){
            showAlertMessage(jsonData["message"]);            
           //alert("Error: Email is already registered");
          } else {
            showAlertMessage(jsonData["message"]);
            //alert("Fatal error");
        }



}
