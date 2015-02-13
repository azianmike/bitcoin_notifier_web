function login(){
        console.log("butts");
        var paramsJSON = {};
        paramsJSON['email'] = document.getElementById("loginEmail").value;
        paramsJSON['password'] = hashPassword(document.getElementById("loginPassword").value);
        postToUrl("/loginJSON/", paramsJSON, loginCallback);
}

function loginCallback(jsonData){
        if(jsonData["success"] == "1"){
          // this means the user has been registere
          window.location.replace("/loginHome/");
          } else if(jsonData["success"] == "0"){
            showAlertMessage(jsonData["message"]);
          } else {
            showAlertMessage(jsonData["message"]);
        }



}
