from django.db.models.signals import post_save
from django.dispatch import receiver

from medtour.applications.models import Application
from medtour.applications.tasks import save_application_for_all_tours


@receiver(post_save, sender=Application)
def bulk_creating_tour_apps(sender, instance, created, **kwargs):
    if created:
        save_application_for_all_tours.delay(name=instance.fullName,
                                             phone=instance.phoneNumber,
                                             obj_type=instance.type,
                                             trip_id=instance.trip_id)
