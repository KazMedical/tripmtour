# views.py
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings

def upload_file_view(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        uploaded_file = request.FILES['upload']

        # Save the uploaded file to the media directory
        with open(f'{settings.MEDIA_ROOT}/{uploaded_file.name}', 'wb') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Get the URL path for accessing the uploaded file using reverse
        file_path = reverse('upload_file_view')
        file_url = request.build_absolute_uri(f'/media/{uploaded_file.name}')  # Replace '/media/' with your media URL path

        # Construct the link with the domain included
        file_link = f'{request.build_absolute_uri(file_path)}?filename={uploaded_file.name}'

        return JsonResponse({'uploaded': 1, 'fileName': uploaded_file.name, 'url': file_url, 'link': file_link})
    else:
        # If the request method is not POST or no file was uploaded,
        # return an error response.
        return JsonResponse({'error': 'Invalid request.'}, status=400)
