# views.py
from django.http import JsonResponse


def upload_file_view(request):
    return JsonResponse({"status": "ok"})
