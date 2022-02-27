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


def checkProject(request):
    client_ip=get_client_ip(request=request)
    return 0



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip