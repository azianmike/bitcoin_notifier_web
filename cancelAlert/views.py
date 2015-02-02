from submitAlertJSON.models import Alert, NumAlertsPerPerson
# Create your views here.
from django.http import HttpResponse
from json import dumps

def index(request, alertIDTemp):
    returnDict={}    
    try:
        alertToDelete = Alert.objects.get(alertID=alertIDTemp)
        person = alertToDelete.person_id
        numAlerts = NumAlertsPerPerson.objects.get(person_id=person)
        numAlerts.decreaseActiveAlerts()
        numAlerts.save()
        alertToDelete.delete()
        returnDict['success'] = 1
        return HttpResponse(dumps(returnDict))        
    except Alert.DoesNotExist:
        returnDict['success'] = -2
        return HttpResponse(dumps(returnDict))

