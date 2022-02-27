from django.core.exceptions import PermissionDenied    
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
class FilterIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        allowed_ips = settings.IP_WHITE_LIST # Authorized ip's
        ip = request.META.get('REMOTE_ADDR') # Get client IP address
        if ip not in allowed_ips:
            raise PermissionDenied # If user is not allowed raise Error
        return None