
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

function postToUrl(url, params){

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
    xmlhttp.open("POST",url,true);
    var paramsString = ""
    for (var key in params) {
        paramsString += key+"="+params[key]
        paramsString += "&"
    }
    if (Object.keys(params).length >1)
    {
        paramsString = paramsString.substring(0, paramsString.length - 1)
    }
    console.log(paramsString)
    //var params = "email="+ document.getElementById("email").value + "&password=" + document.getElementById("password").value;
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.setRequestHeader('X-CSRFToken', csrftoken);
    xmlhttp.send(paramsString);
}


