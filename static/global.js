
function getCookie(name) {
      var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
}
function getURLParameter(name) {
  return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search)||[,""])[1].replace(/\+/g, '%20'))||$
}

function getCondition(conditionId){
    if(conditionId == 1){
        return "New - In Box";
    } else if (conditionId == 2){
        return "Used - Like new";
    } else if (conditionId == 3){
        return "Used - Moderate";
    } else if (conditionId == 4){
        return "Used - Poor";
    } else if (conditionId == 5){
        return "Broken";
    }
    return "Error - incorrect conditionId";
}

function getConditionId(condition){
    if(condition == "New - In Box"){
        return 1;
    } else if (condition == "Used - Like new"){
        return 2;
    } else if (condition == "Used - Moderate"){
        return 3;
    } else if (condition == "Used - Poor"){
        return 4;
    } else if (condition == "Broken"){
        return 5;
    }
}

function checkIfLoggedIn(){
    var csrftoken = getCookie('csrftoken');
    var xmlhttp;
    if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    } else {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function(){
        if (xmlhttp.readyState==4 && xmlhttp.status==200){
            var jsonData = JSON.parse(xmlhttp.responseText);
            if(jsonData["success"] != "1"){
                // this means a user is logged in
                window.location.replace("/");
            } 
        }
    }
    xmlhttp.open("POST","/checkLoginJSON/",true);
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.setRequestHeader('X-CSRFToken', csrftoken);
    xmlhttp.send();
}

function register(){
    if(document.getElementById("password").value == document.getElementById("confirmPassword").value){
        var csrftoken = getCookie('csrftoken');
        var xmlhttp;
        if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
          xmlhttp=new XMLHttpRequest();
        } else {// code for IE6, IE5
            xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange=function(){
            if (xmlhttp.readyState==4 && xmlhttp.status==200){
                var jsonData = JSON.parse(xmlhttp.responseText);
                if(jsonData["success"] == "1"){
                    // this means the user has been registered
                    alert("Success!");
                    window.location.replace("/");
                } else if(jsonData["success"] == "0"){
                    alert("Error: Email is already registered");
                } else {
                    alert("Fatal error");
                } 
            } 
        }
        xmlhttp.open("POST","/registerJSON/",true);
        var params = "email="+ document.getElementById("email").value + "&password=" + document.getElementById("password").value;
        console.log(params);
        xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xmlhttp.setRequestHeader('X-CSRFToken', csrftoken);
        xmlhttp.send(params);
    } else {
        alert("The passwords that you entered do not match!");
    }
}
