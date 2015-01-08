function login(){
        var paramsJSON = {};
        paramsJSON['email'] = document.getElementById("email").value;
        paramsJSON['password'] = hashPassword(document.getElementById("password").value);
        postToUrl("/registerJSON/", paramsJSON);
    } 
 
}

