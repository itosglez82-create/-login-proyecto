from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            # Autentica al usuario usando el sistema interno de Django
            user = authenticate(username=username, password=password)
            
            if user is not None:
                return JsonResponse({'status': 'ok'})
            else:
                return JsonResponse({'status': 'fail'}, status=401)
                
        except json.JSONDecodeError:
            return JsonResponse({'status': 'invalid_json'}, status=400)
            
    return JsonResponse({'status': 'method_not_allowed'}, status=405)