from functools import wraps
from rest_framework import status
from rest_framework.response import Response

def admin_only(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        print("asdfasfaf")
        if not request.user.is_admin:
            
            return Response({"message": "You are not authorized to perform this action."}, status=status.HTTP_403_FORBIDDEN)
        return func(request, *args, **kwargs)
    return wrapper
