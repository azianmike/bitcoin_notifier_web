function login(){
    console.log("enter login");
        var paramsJSON = {};
        paramsJSON['email'] = document.getElementById("loginEmail").value;
        paramsJSON['password'] = hashPassword(document.getElementById("loginPassword").value);
        postToUrl("/loginJSON/", paramsJSON, loginCallback);
}

function loginCallback(jsonData){
        if(jsonData["success"] == "1"){
          // this means the user has been registere
          alert("Success!");
          window.location.replace("/loginHome/");
          } else if(jsonData["success"] == "0"){
            alert("Error: Email does not exist or password is wrong");
          } else {
            alert("Fatal error");
        }



}
