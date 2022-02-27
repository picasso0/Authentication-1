from rest_framework.response import Response
from django.conf import settings
import requests

def response(code,data=[]):
    message,code,status="",205,False
    try:
        response=requests.post(settings.LOG_URL,data={"method_message_id":2222})
        if(response.status_code==200):
            response=response.json()
            message,data,code,status=response['message_text'],data,response['message_code'],False
        else:
            response=response.json()
            message,data,code,status="تابع ریسپانس با مشکل مواجه شده است",response,205,False
    except Exception as e:
        message,data,code,status="تابع ریسپانس با مشکل مواجه شده است",str(e),205,False
        
    return Response({"message":message,"data":data,"code":code,"status":status})
