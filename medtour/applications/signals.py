from django.db.models.signals import post_save
from django.dispatch import receiver

from medtour.applications.models import Application
from medtour.guides.models import GuideProgram
from medtour.tours.models import Tour


def save_application_for_all_objs(name, phone, obj_type, trip_id):
    # TODO: https://mtour.kz/api/dashboard/applications/application/31/change/
    if obj_type == "tours":
        obj = Tour.objects.filter(pk=trip_id)
        if obj.exists():
            obj = obj.first().title
        else:
            obj = "TRIP"
    else:
        obj = GuideProgram.objects.filter(pk=trip_id)
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
    requests.post(url=url, data=data)


@receiver(post_save, sender=Application)
def bulk_creating_tour_apps(sender, instance, created, **kwargs):
    if created:
        save_application_for_all_objs(name=instance.fullName,
                                      phone=instance.phoneNumber,
                                      obj_type=instance.type,
                                      trip_id=instance.trip_id)
