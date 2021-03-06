function getAlerts(){
  var currEmail = getEmail();
  var allAlerts = getUrl("getAlertsJSON/");
  return allAlerts;

}

function parseData(temp){
  var alertType = "";
  //console.log(temp)
  if(temp['textAlert'] && temp['emailAlert']){
    alertType = "email and text";
  }else{
    if(temp['textAlert']){
      alertType = "text";
    }else{
      if(temp['emailAlert']){
        alertType = "email";
      }else{
        alertType = " ";
      }
    }
  }
  var sign = "<";
  if(temp['sign'] == "greaterThan"){
    sign = ">";
  }
  var timeSpan = temp['intervalInSeconds']/60;
  var timeUnits = "minutes";
  if(temp['intervalInSeconds'] % 86400 != temp['intervalInSeconds'])
  {
    timeSpan = temp['intervalInSeconds'] / 86400;
    timeUnits = "days";
  }else{
    if(temp['intervalInSeconds'] % 3600 != temp['intervalInSeconds'])
    {
      timeSpan = temp['intervalInSeconds'] / 3600;
      timeUnits = "hours";
    }
  }

  var dataString = "Alert me via <span class=\"label label-primary\">"+alertType+"</span> when the price is <span class=\"label label-danger\">"+sign+" "+temp['priceThreshold'] +"</span> on <span class=\"label label-success\">"+temp['exchange']+"</span> every <span class=\"label label-warning\">" +timeSpan + " " + timeUnits+"</span>";
  return dataString;
}

function deleteAlertButton(temp){
  //var urlToDelete = "javascript:deleteAlertGetURL(\""+temp['alertID']+"\");"
  var urlToDelete = "javascript:deleteAlertGetURL(&quot;"+temp['alertID']+"&quot;);"
  var dataString = "<button type=\"button\" class=\"btn btn-lg btn-danger\" onclick=\""+urlToDelete+"\">Delete</button>";
  return dataString;
}

function deleteAlertGetURL(alertID){
  //console.log("enter");
  var jsonData = JSON.parse(getUrl("cancelAlert/"+alertID));
  if(jsonData["success"] == 1){
   showAlertMessage(jsonData["message"]);
 }else{
   showAlertMessage(jsonData["message"]);
 }

 onLoad();
}

function populateAlertsPanel(){
  var alertsData = JSON.parse(getAlerts())['data'];
  var finalHtml = "";
  for(var i=0;i<alertsData.length;i++){
    var temp = alertsData[i];
    //console.log(JSON.stringify(temp))
    var dataString = parseData(temp);
    var deleteAlertButtonString = deleteAlertButton(temp)
    finalHtml += "<tr><td>"+dataString+"</td><td>"+deleteAlertButtonString+"</td></tr>";
  }
  $('#alerts-panel-body').html(finalHtml);
}

function submitAlert(){
  //console.log("enter login");
  var paramsJSON = {};
  paramsJSON['sign'] = document.getElementById("sign").value;
  paramsJSON['priceThreshold'] = Number(document.getElementById("priceThreshold").value);
  paramsJSON['emailAlert'] = document.getElementById("emailAlert").checked;
  paramsJSON['textAlert'] = document.getElementById("textAlert").checked;
  paramsJSON['timeIntervalNum'] = Number(document.getElementById("timeIntervalNum").value);
  paramsJSON['timeIntervalUnit'] = document.getElementById("timeIntervalUnit").value;
  paramsJSON['exchange'] = document.getElementById("exchange").value;
  if(!paramsJSON["sign"] || !paramsJSON["priceThreshold"] || !(paramsJSON["emailAlert"]  || paramsJSON["textAlert"]) || !paramsJSON["timeIntervalNum"] || !paramsJSON["timeIntervalUnit"] || !paramsJSON["exchange"] || !(typeof paramsJSON['priceThreshold'] === "number") || !(typeof paramsJSON['timeIntervalNum'] === "number"))
  {
      alert("Fill in all fields correctly");
  }else{
      postToUrl("/submitAlertJSON/", paramsJSON, submitAlertCallback);
  }

}

function submitAlertCallback(jsonData){
  if(jsonData["success"] == "1"){
    showAlertMessage(jsonData["message"]);

  } else if(jsonData["success"] == "0"){
    showAlertMessage(jsonData["message"]);   
  } else if(jsonData["success"] == "-1"){
    showAlertMessage(jsonData["message"]);   
  } else if(jsonData["success"] == "-2"){
    showAlertMessage(jsonData["message"]);   
  }
  else {
    alert("Fatal error");
  }

  onLoad();
}

function populateUserEmail(){
  var email = getUrl("getEmailJSON")
  $('#welcomeBack').html("Welcome back <span class=&quot;highlight&quot;>"+email+"</span>")
}

function getActiveAlerts(){
  var alertsJSON = JSON.parse(getUrl("getNumAlertsJSON"));
  if(alertsJSON["success"] == 1){
    return alertsJSON;
  }else{
    return null
  }
}

function populateNumActiveAlerts(){
  var alertsJSON = getActiveAlerts();
  if(alertsJSON!=null){
    var stringToAppend = "Active Alerts - "+alertsJSON["numAlerts"]+" out of "+alertsJSON["maxAlerts"]+" used."
    $("#alertsPanelTitle").html(stringToAppend)
  }
}

function onLoad(){
  populateAlertsPanel();
  populateUserEmail();
  populateNumActiveAlerts();
}