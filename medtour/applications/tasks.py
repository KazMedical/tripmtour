from celery import shared_task

from medtour.applications.models import TourApplication
from medtour.guides.models import Guide
from medtour.tours.models import Tour


@shared_task
def save_application_for_all_tours(name, phone, obj_type, trip_id):
    # TODO: https://mtour.kz/api/dashboard/applications/application/31/change/
    if obj_type == "tours":
        obj = Tour.objects.filter(pk=trip_id)
        if obj.exists():
            obj = obj.first().title
        else:
            obj = "TRIP"
    else:
        obj = Guide.objects.filter(pk=trip_id)
        if obj.exists():
            obj = obj.first().title
        else:
            obj = "TRIP"
    import requests
    from django.conf import settings
    data = {
        "chat_id": settings.APPLICATION_SEND_BOT_GROUP_ID,
        "text": "Новая заявка: \n"
                f"Объект: {obj}\n"
                f"Имя: {name}\n"
                f"Телефон: {phone}\n"
    }
    url = f"https://api.telegram.org/bot{settings.APPLICATION_SEND_BOT_TOKEN}/sendMessage"
    x = requests.post(url=url,
                      data=data)
    return x.text
