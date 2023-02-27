import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import User
from .encoders import UserEncoder

# Create your views here.
@require_http_methods(["GET", "POST"])
def users_list(request):
    if request.method == "GET":
        users = User.objects.all()
        return JsonResponse(
            {'users': users},
            encoder=UserEncoder
        )
    else:
        content = json.loads(request.body)
        user = User.objects.create_user(**content)
        return JsonResponse(
            {"user created": user},
            encoder=UserEncoder,
            safe=False
        )
