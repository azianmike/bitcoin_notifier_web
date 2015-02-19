
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

function postToUrl(url, params, callbackFunction){

    var csrftoken = getCookie('csrftoken');
    var xmlhttp;
    if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    } else {// code for IE6, IE5
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function(){
            if (xmlhttp.readyState==4 && xmlhttp.status==200){
                var jsonData = JSON.parse(xmlhttp.responseText)
                callbackFunction(jsonData);
            }
    }
        ;



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
    //var params = "email="+ document.getElementById("email").value + "&password=" + document.getElementById("password").value;
    xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xmlhttp.setRequestHeader('X-CSRFToken', csrftoken);
    xmlhttp.send(paramsString);
}

function getUrl(theUrl){
    var indexOfMainUrl = theUrl.indexOf("http://www.coinsniff.com/");
    if(indexOfMainUrl!= -1)
    {
        var xmlHttp = null;
        xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", theUrl, false );
        xmlHttp.send( null );
        return xmlHttp.responseText;
    }else{
        var xmlHttp = null;
        xmlHttp = new XMLHttpRequest();
        xmlHttp.open( "GET", "http://www.coinsniff.com/"+theUrl, false );
        xmlHttp.send( null );
        return xmlHttp.responseText;
    }
}

function getEmail(){
    return getUrl("getEmailJSON")
}

function logout(){
  console.log("enter");
  var response = getUrl("logout/");
  window.location.replace("/");

}

function showAlertMessage(message)
{
    var htmlTemp = "<div class=alert&#32;alert-info role=alert id=alertBox>"+
    "<button type=button class=close data-dismiss=alert>×<\/button>"+message+"</div>"
    $("#alertBox").html(htmlTemp);
    $("#alertBox").show();

}


